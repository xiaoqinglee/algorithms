import collections.abc
from functools import reduce

# # SegmentTree 的意图：
# 一个固定长度的数组， 数组中的不定某个元素和不定某个区间数据发生更新动作，
# 想用logN的复杂度查询任意区间内的元素统计信息， 比如元素的和，最大元素值，最小元素值。
#
# 如果不借助任何数据结构，时间复杂度是n。
# 使用前缀和和哈希表可以做大常数时间复杂度，但是不允许数组元素发生变化。


# SegmentTree 的是个满二叉树，只有最后一行存在空Node， 所以我们可以使用数组存储，使用数组运算寻找孩子节点。
# 满二叉树意味着 SegmentTree能很方便的持久化
# （使用连个list，一个list存储segment_left_end_index, 一个存segment_right_end_index， 空Node在两个数组中都为nil）
# 源数组长度为n，最坏情况下，当n >= 3时，总的非空Node个数为 4n-5
# （最后一行有连个节点， 到第二行有n-2个叶子节点，1个非叶子节点， 可得最后一行node空间一共有2(n-1), 可得总节点数4n-5）
# 所以使用4n
# 这里的实现不使用数组存储了


ListElemVal = int


class Segment:
    def __init__(self, tree, left, right, val=None, left_child=None, right_child=None):
        self.tree = tree
        self.segment_left_idx: int = left
        self.segment_right_idx: int = right
        self.val: ListElemVal | None = None
        self.left_child: Segment | None = left_child
        self.right_child: Segment | None = right_child

    def update_one(self, index: int, new_val: ListElemVal) -> None:
        self.update_segment(index, index, new_val)

    # 到底
    def update_segment(self, left: int, right: int, new_val: ListElemVal) -> None:
        if self.segment_left_idx == self.segment_right_idx:
            self.val = new_val
            return
        if right <= self.left_child.segment_right_idx:
            self.left_child.update_segment(left, right, new_val)
        elif self.right_child.segment_left_idx <= left:
            self.right_child.update_segment(left, right, new_val)
        else:
            self.left_child.update_segment(left, self.left_child.segment_right_idx, new_val)
            self.right_child.update_segment(self.right_child.segment_left_idx, right, new_val)
        self.val = reduce(self.tree.list_reducing_func,
                          map(self.tree.list_element_mapping_func,
                              [self.left_child.val, self.right_child.val]))

    def query_one(self, index: int) -> ListElemVal:
        return self.query_segment(index, index)

    # 不到底
    def query_segment(self, left: int, right: int) -> ListElemVal:
        if self.segment_left_idx == self.segment_right_idx:
            return self.val
        if self.segment_left_idx == left and self.segment_right_idx == right:
            return self.val
        if right <= self.left_child.segment_right_idx:
            return self.left_child.query_segment(left, right)
        elif self.right_child.segment_left_idx <= left:
            return self.right_child.query_segment(left, right)
        else:
            left_hand_side = self.left_child.query_segment(left, self.left_child.segment_right_idx)
            right_hand_side = self.right_child.query_segment(self.right_child.segment_left_idx, right)
            return reduce(self.tree.list_reducing_func,
                              map(self.tree.list_element_mapping_func,
                                  [left_hand_side, right_hand_side]))


class SegmentTree:
    def __init__(self,
                 elements: list[ListElemVal],
                 list_element_mapping_func: collections.abc.Callable[[ListElemVal], ListElemVal],
                 list_reducing_func: collections.abc.Callable[[ListElemVal, ListElemVal], ListElemVal]):

        self.elements = elements.copy()
        self.list_element_mapping_func = list_element_mapping_func
        self.list_reducing_func = list_reducing_func

        def build_tree(left: int, right: int) -> Segment:
            seg = Segment(self, left, right)
            if left == right:
                seg.val = self.elements[left]
                return seg
            mid = (left + right) // 2
            left_child = build_tree(left, mid)
            right_child = build_tree(mid + 1, right)
            seg.left_child = left_child
            seg.right_child = right_child
            seg.val = reduce(self.list_reducing_func,
                             map(self.list_element_mapping_func,
                                 [seg.left_child.val, seg.right_child.val]))
            return seg

        self.root: Segment = build_tree(0, len(self.elements)-1)

