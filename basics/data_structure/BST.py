from typing import Any


class BST:
    def __init__(self, key, val, left=None, right=None):
        self.key: int = key
        self.val: Any = val
        self.left: BST | None = left
        self.right: BST | None = right

    def search(self, key: int) -> Any:
        if key == self.key:
            return self.val
        elif key < self.key and self.left is not None:
            return self.left.search(key)
        elif key > self.key and self.right is not None:
            return self.right.search(key)
        else:
            return None

    def insert(self, key: int, val: Any) -> None:
        if key == self.key:
            self.val = val
        elif key < self.key:
            if self.left is not None:
                self.left.insert(key, val)
            else:
                self.left = BST(key, val)
        elif key > self.key:
            if self.right is not None:
                self.right.insert(key, val)
            else:
                self.right = BST(key, val)

    @classmethod
    def remove(cls, root, key: int):  # 调用方式 tree = BST.remove(tree, key)

        def _pre_node(tree):  # 要求 tree 一定存在 pre node
            node = tree.left
            while node is not None and node.right is not None:
                node = node.right
            return node

        def _remove(tree):  # tree is not None
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
