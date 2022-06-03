from pypkg.datatype import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result: list[list[int]] = []
        if root is None:
            return result
        from collections import deque
        queue: deque[TreeNode] = deque()
        queue.append(root)
        finished_level = 0
        while len(queue) > 0:
            n_nodes_of_same_level = len(queue)
            nodes_of_same_level: list[int] = []
            for i in range(n_nodes_of_same_level):
                node = queue.popleft()
                nodes_of_same_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(nodes_of_same_level)
            finished_level += 1
        print("层数：", finished_level)
        return result
