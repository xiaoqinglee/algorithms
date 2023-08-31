# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pkg.data_structure import TreeNode


# https://leetcode.cn/problems/delete-node-in-a-bst
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        def _pre_node(tree: TreeNode) -> TreeNode:  # 要求 tree 一定存在 pre node
            node = tree.left
            while node is not None and node.right is not None:
                node = node.right
            return node

        def _remove(tree: TreeNode) -> TreeNode | None:
            if tree.left is None:
                return tree.right
            if tree.right is None:
                return tree.left
            pre = _pre_node(tree)
            pre.right = tree.right

            # no need to worry about the value of "tree", it will get collected when no reference points to it.
            # https://docs.python.org/zh-cn/3/library/sys.html#sys.getrefcount

            return tree.left

        if root is None:
            return None

        if key == root.val:
            return _remove(root)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        else:  # key > root.val
            root.right = self.deleteNode(root.right, key)
            return root
