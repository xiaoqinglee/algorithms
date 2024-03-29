from collections import defaultdict


class Trie:
    ARRAY_LEN = 26

    def __init__(self):
        self.is_terminal: bool = False
        self.full_word: str | None = None  # 仅当self.is_terminal为True时有意义
        self.full_word_count: int = 0  # 仅当self.is_terminal为True时有意义
        self.children: list[Trie | None] = [None] * self.ARRAY_LEN
        # 该 trie 有多少个单词(不含当前 trie node 本身), 不一定等于children数组中非 None 元素个数
        self.children_have_n_words: int = 0

    def insert(self, word: str) -> None:
        node: Trie = self
        for char in word:
            node.children_have_n_words += 1
            child: Trie | None = node.children[ord(char) - ord('a')]
            if child is None:
                # print("inserting", char)
                child = Trie()
                node.children[ord(char) - ord('a')] = child
            node = child
        if node.is_terminal:
            node.full_word_count += 1
        else:
            node.is_terminal = True
            node.full_word = word
            node.full_word_count = 1

    def delete(self, word: str) -> None:
        parent_nodes_to_update: list[Trie] = []  # root 在这个栈里， 但是 root node 永远不会被 delete
        paths_leading_to_child_node: list[str] = []

        node: Trie = self
        for char in word:
            parent_nodes_to_update.append(node)
            paths_leading_to_child_node.append(char)
            child: Trie | None = node.children[ord(char) - ord('a')]
            if child is None:
                raise "word not in trie"
            node = child

        if not node.is_terminal:
            raise "word not in trie"
        if node.full_word_count > 1:
            node.full_word_count -= 1
        elif node.full_word_count == 1:
            node.is_terminal = False
        else:  # 这种情况不存在
            pass

        child_is_kept: bool | None = None
        if not node.is_terminal and node.children_have_n_words == 0:
            # print("deleting node", node.full_word)
            child_is_kept = False
        else:
            child_is_kept = True

        while len(parent_nodes_to_update) > 0:
            node: Trie = parent_nodes_to_update.pop()
            path_leading_to_child: str = paths_leading_to_child_node.pop()
            node.children_have_n_words -= 1

            if child_is_kept:
                continue
            # print("deleting path", path_leading_to_child)
            node.children[ord(path_leading_to_child)-ord('a')] = None

            if not node.is_terminal and node.children_have_n_words == 0:
                # print("deleting node", node.full_word)
                child_is_kept = False
            else:
                child_is_kept = True

    def search(self, word: str) -> bool:
        exists: bool = False
        node: Trie = self
        for char in word:
            node: Trie | None = node.children[ord(char) - ord('a')]
            if node is None:
                return exists
        if node.is_terminal:
            exists = True
            return exists
        return exists

    def contains_prefix(self, prefix: str) -> bool:
        exists: bool = False
        node: Trie = self
        for char in prefix:
            node: Trie | None = node.children[ord(char) - ord('a')]
            if node is None:
                return exists
        exists = node.is_terminal or node.children_have_n_words > 0
        return exists


# 叶子节点的数据为全null数组
# 叶子节点代表的字符串的最后一个字符是什么这个信息存在parent的children数组里面
# 一个空树只有一个root节点，self即是root


class SimpleTrie:
    def __init__(self):
        self.next: defaultdict[str, SimpleTrie] = defaultdict(SimpleTrie)
        self.is_terminal = False
        self.terminal_value: str | None = None
        self.terminal_value_count: int | None = None

    def insert(self, word: str) -> None:
        current_trie = self
        for c in word:
            current_trie = current_trie.next[c]
        if not current_trie.is_terminal:
            current_trie.is_terminal = True
            current_trie.terminal_value = word
            current_trie.terminal_value_count = 1
        else:
            current_trie.terminal_value_count += 1

    def search(self, word: str) -> bool:  # 无副作用
        current_trie = self
        for c in word:
            # defaultdict(default_factory=None, /, [...]) --> dict with default factory
            #
            #         The default factory is called without arguments to produce
            #         a new value when a key is not present, in __getitem__ only.
            if c not in current_trie.next:
                return False
            current_trie = current_trie.next[c]
        return current_trie.is_terminal

    def contains_prefix(self, word: str) -> bool:  # 无副作用
        current_trie = self
        for c in word:
            if c not in current_trie.next:
                return False
            current_trie = current_trie.next[c]
        return current_trie.is_terminal or len(current_trie.next) > 0


if __name__ == '__main__':
    simple_trie = SimpleTrie()
    print(simple_trie.search(""))
    print(simple_trie.contains_prefix(""))
    print(simple_trie.search("4"))
    print(simple_trie.contains_prefix("4"))
    print(simple_trie.search("42"))
    print(simple_trie.contains_prefix("42"))

    print("===============================")
    simple_trie.insert("")
    simple_trie.insert("42")
    print(simple_trie.search(""))
    print(simple_trie.contains_prefix(""))
    print(simple_trie.search("4"))
    print(simple_trie.contains_prefix("4"))
    print(simple_trie.search("42"))
    print(simple_trie.contains_prefix("42"))

    print("===============================")
    simple_trie.insert("")
    simple_trie.insert("42")
    print(simple_trie.search(""))
    print(simple_trie.contains_prefix(""))
    print(simple_trie.search("4"))
    print(simple_trie.contains_prefix("4"))
    print(simple_trie.search("42"))
    print(simple_trie.contains_prefix("42"))
