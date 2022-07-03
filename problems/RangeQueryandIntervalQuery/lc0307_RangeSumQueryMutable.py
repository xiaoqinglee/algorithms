from basics.data_structure.SegmentTree import SegmentTree


class NumArray:

    def __init__(self, nums: list[int]):
        self.tree = SegmentTree(elements=nums,
                                list_element_mapping_func=lambda x: x,
                                list_reducing_func=lambda x, y: x + y)

    def update(self, index: int, val: int) -> None:
        self.tree.root.update_one(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.root.query_segment(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
