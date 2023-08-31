"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.cn/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
class Solution:
    def treeToDoublyList(self, root: Node | None) -> Node | None:
        if root is None:
            return root

        inorder_nodes: list[Node] = []

        def traverse(node: Node | None) -> None:
            if node is None:
                return
            traverse(node.left)
            inorder_nodes.append(node)
            traverse(node.right)

        traverse(root)

        head: Node | None = None
        for i, node in enumerate(inorder_nodes):
            if i == 0:
                head = node
                node.left = node
                node.right = node
            else:
                last_node: Node = head.left

                node.right = head
                node.left = last_node

                last_node.right = node

                head.left = node

        return head
