# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pkg.data_structure import TreeNode


# https://leetcode.cn/problems/diameter-of-binary-tree
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        # 处理完左右子树然后处理根
        if root is None:
            return 0

        diameter: int = 0

        def single_path_length(node: TreeNode) -> int:
            assert node is not None

            left_single_path_length: int = 0
            right_single_path_length: int = 0

            if node.left is not None:
                left_single_path_length = 1 + single_path_length(node.left)
            if node.right is not None:
                right_single_path_length = 1 + single_path_length(node.right)

            diameter_candidate = left_single_path_length + right_single_path_length
            nonlocal diameter
            diameter = max(diameter, diameter_candidate)

            return max(left_single_path_length, right_single_path_length)

        single_path_length(root)
        return diameter
