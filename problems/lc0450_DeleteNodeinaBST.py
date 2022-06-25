from pkg.data_structure import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        def _pre_node(tree):  # 要求 tree 一定存在 pre node
            node = tree.left
            while node is not None and node.right is not None:
                node = node.right
            return node

        def _remove(tree):
            if tree.left is None:
                return tree.right
            if tree.right is None:
                return tree.left
            pre = _pre_node(tree)
            pre.right = tree.right
            return tree.left

        if root is None:
            return None
        elif key == root.val:
            return _remove(root)
        elif key < root.val and root.left is not None:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val and root.right is not None:
            root.right = self.deleteNode(root.right, key)
            return root
        return root
