# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pkg.data_structure import TreeNode


# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        def build_tree(left, right) -> TreeNode | None:

            if left > right:
                return None
            elif left == right:
                return TreeNode(nums[left])
            else:
                mid = (left + right) // 2
                root = TreeNode(nums[mid])
                root.left = build_tree(left, mid-1)
                root.right = build_tree(mid+1, right)
                return root

        return build_tree(0, len(nums)-1)
