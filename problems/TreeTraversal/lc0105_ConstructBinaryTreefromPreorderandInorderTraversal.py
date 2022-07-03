from pkg.data_structure import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder) == 0:
            return None

        value_to_inorder_index_dict = {value: inorder_index
                                       for inorder_index, value in enumerate(inorder)}
        root_value = preorder[0]
        root_node_index = value_to_inorder_index_dict[root_value]

        left_tree_preorder = preorder[1: root_node_index + 1]
        left_tree_inorder = inorder[:root_node_index]
        left_tree: TreeNode | None = self.buildTree(left_tree_preorder, left_tree_inorder)

        right_tree_preorder = preorder[root_node_index + 1:]
        right_tree_inorder = inorder[root_node_index + 1:]
        right_tree: TreeNode | None = self.buildTree(right_tree_preorder, right_tree_inorder)

        root = TreeNode(val=root_value, left=left_tree, right=right_tree)
        return root
