from pypkg.datatype import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        def is_mirror(tree1: TreeNode | None, tree2: TreeNode | None) -> bool:
            if tree1 is None and tree2 is None:
                return True

            return ((tree1 is not None and tree2 is not None)
                    and tree1.val == tree2.val
                    and is_mirror(tree1.left, tree2.right)
                    and is_mirror(tree1.right, tree2.left))

        return is_mirror(root.left, root.right)
