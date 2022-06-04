from pypkg.datatype import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        # 中序遍历，先处理完左右子树然后处理根
        # 处理根节点时，计算当前根节点到叶子节点的路径长度path_length
        # 题目所求的直径是所有根节点中（左子树的path_length + 右子树path_length + 2）值最大的那个根节点的这个值

        diameter: int = 0

        def path_length(node: TreeNode | None) -> int:
            if node is None or (node.left is None and node.right is None):
                return 0
            left_child_path_length = path_length(node.left)
            right_child_path_length = path_length(node.right)
            path_length_ = max(left_child_path_length, right_child_path_length) + 1

            diameter_candidate = left_child_path_length + right_child_path_length + (
                    2 if node.left is not None and node.right is not None else 1
                )
            nonlocal diameter
            if diameter_candidate > diameter:
                diameter = diameter_candidate

            return path_length_

        path_length(root)
        return diameter
