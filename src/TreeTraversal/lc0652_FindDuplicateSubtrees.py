# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pkg.data_structure import TreeNode


# https://leetcode.cn/problems/find-duplicate-subtrees
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode]:

        node_to_serialized_node: dict[TreeNode | None, str] = {None: "nil"}
        serialized_node_to_nodes: dict[str, list[TreeNode | None]] = {"nil": [None]}

        def find_dup(node: TreeNode | None) -> None:
            if node is None:
                return
            find_dup(node.left)
            find_dup(node.right)
            serialized_node: str = ("(" + node_to_serialized_node[node.left] + ")" +
                                    str(node.val) +
                                    "(" + node_to_serialized_node[node.right] + ")")
            node_to_serialized_node[node] = serialized_node
            serialized_node_to_nodes.setdefault(serialized_node, []).append(node)

        find_dup(root)
        return [v[0] for k, v in serialized_node_to_nodes.items() if len(v) > 1]
