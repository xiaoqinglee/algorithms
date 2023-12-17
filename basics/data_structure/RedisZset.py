class ZSet:
    def __init__(self, elem_to_score=None):
        if elem_to_score is None:
            elem_to_score = {}
        self.elem_to_score: dict[str, float] = elem_to_score.copy()
        self.skiplist: Skiplist = Skiplist()
        for elem, score in elem_to_score.items():
            self.skiplist.insert(score=score, zset_element=elem)

    def __len__(self):
        return len(self.elem_to_score)

    def insert(self, score: float, zset_element: str) -> None:
        if zset_element in self.elem_to_score:
            self.remove(zset_element=zset_element)
        self.elem_to_score[zset_element] = score
        self.skiplist.insert(score=score, zset_element=zset_element)

    def remove(self, zset_element: str) -> None:
        if zset_element not in self.elem_to_score:
            return
        self.skiplist.remove(score=self.elem_to_score[zset_element], zset_element=zset_element)
        del self.elem_to_score[zset_element]

    def get_element_rank(self, zset_element: str) -> int | None:
        if zset_element not in self.elem_to_score:
            return
        score = self.elem_to_score[zset_element]
        return self.skiplist.get_element_rank(score, zset_element)

    def search_element_by_rank(self, rank: int) -> tuple[float, str] | None:
        if not 1 <= rank <= len(self.elem_to_score):
            return
        return self.skiplist.search_element_by_rank(rank)


class SkiplistLevel:
    def __init__(self):
        self.forward: SkiplistNode | None = None
        self.span: int = 0


class SkiplistNode:
    def __init__(self, level_count: int, score: float, zset_element: str | None):
        self.elem: str | None = zset_element
        self.score: float = score
        self.backward: SkiplistNode | None = None
        self.levels: list[SkiplistLevel] = [SkiplistLevel() for i in range(level_count)]

    def __repr__(self):
        return repr({
            "elem": self.elem,
            "score": self.score,
            "levels[{}]".format(len(self.levels)): [level.span for level in self.levels]
        })


class Skiplist:
    SKIPLIST_MAX_LEVEL = 32
    LEVEL_GROW_CHANCE = 1/2

    @classmethod
    def gen_random_node_level(cls) -> int:
        import random
        level = 1
        while True:
            random_float = random.uniform(0, 1)
            if random_float > cls.LEVEL_GROW_CHANCE:
                return min(level, cls.SKIPLIST_MAX_LEVEL)
            level += 1

    def __init__(self):
        self.dummy_header: SkiplistNode = \
            SkiplistNode(level_count=self.SKIPLIST_MAX_LEVEL, score=0, zset_element=None)
        self.tail: SkiplistNode | None = None
        self.length: int = 0
        self.instance_max_level: int = 1

    # elem 必须不存在于skiplist中
    # Insert a new node in the skiplist. Assumes the element does not already exist (up to the caller to enforce that).
    def insert(self, score: float, zset_element: str) -> None:
        # 将一个Node看成(score, element_string)的二元组，寻找最后一个小于(score, zset_element)的二元组对应的node
        nodes_to_update: list[SkiplistNode | None] = [None] * self.SKIPLIST_MAX_LEVEL
        node_ranks: list[int | None] = [None] * self.SKIPLIST_MAX_LEVEL
        x: SkiplistNode = self.dummy_header

        for i in range(self.instance_max_level-1, -1, -1):
            if i == self.instance_max_level-1:
                node_ranks[i] = 0
            else:
                node_ranks[i] = node_ranks[i+1]
            while (x.levels[i].forward is not None and
                   (x.levels[i].forward.score, x.levels[i].forward.elem) < (score, zset_element)):
                node_ranks[i] += x.levels[i].span
                x = x.levels[i].forward
            # x是当前层待插入目标节点的前驱节点
            # x 可能是self.dummy_header
            nodes_to_update[i] = x

        new_node_level: int = self.gen_random_node_level()
        if new_node_level > self.instance_max_level:
            for i in range(self.instance_max_level, new_node_level):
                node_ranks[i] = 0
                nodes_to_update[i] = self.dummy_header
                nodes_to_update[i].levels[i].span = self.length
            self.instance_max_level = new_node_level

        x = SkiplistNode(level_count=new_node_level, score=score, zset_element=zset_element)
        for i in range(new_node_level):
            x.levels[i].forward = nodes_to_update[i].levels[i].forward
            nodes_to_update[i].levels[i].forward = x
            x.levels[i].span = (nodes_to_update[i].levels[i].span + 1) - ((node_ranks[0] + 1) - node_ranks[i])
            nodes_to_update[i].levels[i].span = (node_ranks[0] + 1) - node_ranks[i]

        for i in range(new_node_level, self.instance_max_level):
            nodes_to_update[i].levels[i].span += 1

        if nodes_to_update[0] is not self.dummy_header:
            x.backward = nodes_to_update[0]
        if x.levels[0].forward is not None:
            x.levels[0].forward.backward = x
        else:
            self.tail = x

        self.length += 1

    def remove(self, score: float, zset_element: str) -> None:
        # 重复代码开始：
        # 将一个Node看成(score, element_string)的二元组，寻找最后一个小于(score, zset_element)的二元组对应的node
        nodes_to_update: list[SkiplistNode | None] = [None] * self.SKIPLIST_MAX_LEVEL
        node_ranks: list[int | None] = [None] * self.SKIPLIST_MAX_LEVEL
        x: SkiplistNode = self.dummy_header

        for i in range(self.instance_max_level-1, -1, -1):
            if i == self.instance_max_level-1:
                node_ranks[i] = 0
            else:
                node_ranks[i] = node_ranks[i+1]
            while (x.levels[i].forward is not None and
                   (x.levels[i].forward.score, x.levels[i].forward.elem) < (score, zset_element)):
                node_ranks[i] += x.levels[i].span
                x = x.levels[i].forward
            # x是当前层待移除目标节点的前驱节点
            # x 可能是self.dummy_header
            nodes_to_update[i] = x
        # 重复代码结束

        x = x.levels[0].forward
        # 现在，x 肯定不是self.dummy_header了
        if not (x is not None and (x.score, x.elem) == (score, zset_element)):  # 没找到该node
            return

        for i in range(self.instance_max_level):
            if nodes_to_update[i].levels[i].forward == x:
                nodes_to_update[i].levels[i].span = \
                    nodes_to_update[i].levels[i].span + x.levels[i].span - 1
                nodes_to_update[i].levels[i].forward = x.levels[i].forward
            else:
                nodes_to_update[i].levels[i].span -= 1

        if x.levels[0].forward is not None:
            x.levels[0].forward.backward = x.backward
        else:
            self.tail = x.backward

        while (self.instance_max_level > 1 and
               self.dummy_header.levels[self.instance_max_level - 1].forward is None):
            self.instance_max_level -= 1

        self.length -= 1

    def get_element_rank(self, score: float, zset_element: str) -> int | None:
        node_rank: int = 0
        x: SkiplistNode = self.dummy_header
        for i in range(self.instance_max_level-1, -1, -1):
            while (x.levels[i].forward is not None and
                   (x.levels[i].forward.score, x.levels[i].forward.elem) <= (score, zset_element)):
                node_rank += x.levels[i].span
                x = x.levels[i].forward
            # x 可能是self.dummy_header
        # x 仍然可能是self.dummy_header
        if x != self.dummy_header and (x.score, x.elem) == (score, zset_element):
            return node_rank
        # 没有找到该node
        return

    def search_element_by_rank(self, rank: int) -> tuple[float, str] | None:
        if not 1 <= rank <= self.length:
            return
        node_rank: int = 0
        x: SkiplistNode = self.dummy_header
        for i in range(self.instance_max_level-1, -1, -1):
            while (x.levels[i].forward is not None and
                   node_rank + x.levels[i].span <= rank):
                node_rank += x.levels[i].span
                x = x.levels[i].forward
            # x 可能是self.dummy_header
        # 现在，x 肯定不是self.dummy_header了，因为rank > 1 而且我们已经访问过第0层了
        # 此时 rank == node_rank,
        return x.score, x.elem


# https://segmentfault.com/a/1190000037435499
# 在Redis中，SkipList主要作为Sorted Set的底层数据结构，
# 它的实现几乎是William Pugh在论文中描述的原始算法的C语言版的翻译。
# 除了对以下三个方面进行了修改:
#
# 该实现允许重复的分数（score）
# 同时通过键（即score）和对应的元素进行比较
# 有一个向前指针，所以第一层是双向链表，以此允许从尾到头的遍历。


def test_zset():
    print("============================================")
    zset = ZSet({
        char: int(char) for char in "0123456789"
    })
    for k, v in {char: ord(char) - ord('a') for char in "abcde"}.items():
        zset.insert(v, k)
    for i in range(15):
        print(zset.search_element_by_rank(i+1))

    print("============================================")
    for k, v in {char: (ord(char) - ord('a')) * 2 for char in "abcde"}.items():
        zset.insert(v, k)
    for i in range(15):
        print(zset.search_element_by_rank(i+1))

    print("============================================")
    li = []
    node = zset.skiplist.tail
    while node is not None:
        li.append(node)
        node = node.backward

    from pprint import pprint
    pprint([node for node in list(reversed(li))])

    print("============================================")
    print(zset.get_element_rank('0'))
    print(zset.get_element_rank('a'))
    print(zset.get_element_rank('1'))
    print(zset.get_element_rank('2'))
    print(zset.get_element_rank('b'))
    print(zset.get_element_rank('3'))
    print(zset.get_element_rank('4'))
    print(zset.get_element_rank('c'))
    print(len(zset))

    print("============================================")
    print(zset.remove('0'))
    print(zset.remove('b'))
    print(zset.remove('9'))

    print(zset.get_element_rank('0'))
    print(zset.get_element_rank('a'))
    print(zset.get_element_rank('1'))
    print(zset.get_element_rank('2'))
    print(zset.get_element_rank('b'))
    print(zset.get_element_rank('3'))
    print(zset.get_element_rank('4'))
    print(zset.get_element_rank('c'))
    print(zset.get_element_rank('9'))

    print(len(zset))

    print("============================================")
    zset = ZSet({
        char: int(char) for char in "0"
    })

    print(zset.remove('0'))
    print(zset.get_element_rank('0'))
    print(zset.search_element_by_rank(1))

    print(zset.insert(-100, '0'))
    print(zset.get_element_rank('0'))
    print(zset.search_element_by_rank(1))

    print(zset.remove('0'))

    print(zset.remove('0'))
    print(zset.get_element_rank('0'))
    print(zset.search_element_by_rank(1))

    print(len(zset))

    print("============================================")
    zset = ZSet({
    })

    print(zset.skiplist.remove(-100, '0'))
    print(zset.skiplist.get_element_rank(-100, '0'))
    print(zset.skiplist.search_element_by_rank(1))

    print(zset.skiplist.insert(-100, '0'))
    print(zset.skiplist.get_element_rank(-100, '0'))
    print(zset.skiplist.search_element_by_rank(1))

    print(zset.skiplist.remove(-100, '0'))

    print(zset.skiplist.remove(-100, '0'))
    print(zset.skiplist.get_element_rank(-100, '0'))
    print(zset.skiplist.search_element_by_rank(1))

    print(len(zset))


if __name__ == '__main__':
    test_zset()
