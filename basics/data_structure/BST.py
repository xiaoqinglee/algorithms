from typing import Any


class BSTNode:
    def __init__(self, key: int, val: Any):
        self.key = key
        self.val = val
        self.left: BST = BST()
        self.right: BST = BST()


class BST:
    def __init__(self):
        self.root: BSTNode | None = None

    def insert(self, key: int, val: Any = None) -> None:
        if self.root is None:
            self.root = BSTNode(key, val)
            return
        if key == self.root.key:
            self.root.val = val
        elif key < self.root.key:
            self.root.left.insert(key, val)
        else:
            self.root.right.insert(key, val)

    def search(self, key: int) -> Any:
        if self.root is None:
            return None
        if key == self.root.key:
            return self.root.val
        elif key < self.root.key:
            return self.root.left.search(key)
        else:
            return self.root.right.search(key)

    def delete(self, key: int) -> None:

        def _pre_node(node: BSTNode) -> BSTNode:  # 要求 node 一定存在 pre node
            node = node.left.root
            while node is not None and node.right.root is not None:
                node = node.right.root
            return node

        def _remove(node: BSTNode) -> BSTNode | None:
            if node.left.root is None:
                return node.right.root
            if node.right.root is None:
                return node.left.root
            pre = _pre_node(node)
            pre.right.root = node.right.root

            # no need to worry about the value of "node", it will get collected when no reference points to it.
            # https://docs.python.org/zh-cn/3/library/sys.html#sys.getrefcount

            return node.left.root

        if self.root is None:
            return

        if key == self.root.key:
            self.root = _remove(self.root)
        elif key < self.root.key:
            self.root.left.delete(key)
        else:
            self.root.right.delete(key)
