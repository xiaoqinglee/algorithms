from typing import Any


class BST:
    def __init__(self, key, val, left=None, right=None):
        self.key: int = key
        self.val: Any = val
        self.left: BST = left
        self.right: BST = right

    def search(self, key: int) -> Any:
        if key == self.key:
            return self.val
        elif key < self.key and self.left is not None:
            return self.left.search(key)
        elif key > self.key and self.right is not None:
            return self.right.search(key)
        return None

    def insert(self, key: int, val: Any) -> None:
        if key == self.key:
            self.val = val
            return
        elif key < self.key and self.left is not None:
            return self.left.insert(key, val)
        elif key > self.key and self.right is not None:
            return self.right.insert(key, val)

    @classmethod
    def remove(cls, root, key: int):  # 调用方式 tree = BST.remove(tree, key)

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
        elif key == root.key:
            return _remove(root)
        elif key < root.key and root.left is not None:
            root.left = BST.remove(root.left, key)
            return root
        elif key > root.key and root.right is not None:
            root.right = BST.remove(root.right, key)
            return root
        return root
