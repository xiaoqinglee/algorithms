# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from pkg.data_structure import TreeNode


# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree
class Codec:

    def serialize(self, root: TreeNode | None) -> str:
        nodes: list[TreeNode | None] = []
        from collections import deque
        queue: deque[TreeNode | None] = deque()
        queue.append(root)
        while len(queue) > 0:
            node: TreeNode | None = queue.popleft()
            nodes.append(node)
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
        while len(nodes) > 0 and nodes[-1] is None:
            nodes.pop()

        string = "[" + ", ".join("null" if x is None else str(x.val) for x in nodes) + "]"
        return string

    def deserialize(self, data: str) -> TreeNode | None:
        from collections import deque
        nodes: deque[TreeNode | None] = deque()

        current: list[str] = []
        for char in data:
            if char in '[ ':
                # do nothing
                pass
            elif char in ",]":
                if len(current) > 0:
                    current_node: str = "".join(current)
                    if current_node == "null":
                        nodes.append(None)
                    else:
                        val = int(current_node)
                        nodes.append(TreeNode(val=val))
                    current = []
                else:
                    # data is "[]"
                    pass
            else:
                current.append(char)

        if len(nodes) == 0:
            return None

        root: TreeNode | None = None
        nodes_in_prev_level: list[TreeNode | None] = [nodes.popleft()]
        nodes_in_curr_level: list[TreeNode | None] = []

        while True:
            for index, node in enumerate(nodes_in_prev_level):
                if root is None:
                    root = node
                if node is None:
                    continue

                left: TreeNode | None = nodes.popleft() if len(nodes) > 0 else None
                right: TreeNode | None = nodes.popleft() if len(nodes) > 0 else None
                node.left = left
                node.right = right

                nodes_in_curr_level.append(left)
                nodes_in_curr_level.append(right)

            if len(nodes) == 0:
                break
            nodes_in_prev_level = nodes_in_curr_level
            nodes_in_curr_level = []

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
