from pkg.data_structure import TreeNode


# N 叉树的 node
class NaryTreeNode:
    def __init__(self, val, children: list = None):
        self.val: int = val
        self.children: list[NaryTreeNode] = children or []


class Codec:

    # Encodes an n-ary tree to a binary tree
    def encode(self, root: NaryTreeNode | None) -> TreeNode | None:
        if root is None:
            return None
        binary_tree_root = TreeNode(val=root.val)
        binary_tree_root.left = self.encode_from_forest(root.children)
        return binary_tree_root

    # Decodes your binary tree to an n-ary tree
    def decode(self, root: TreeNode | None) -> NaryTreeNode | None:
        if root is None:
            return None
        if root.right is not None:
            raise "解码后会变成森林而不是1棵N叉树"
        nary_tree_root = NaryTreeNode(val=root.val)
        nary_tree_root.children = self.decode_to_forest(root.left)
        return nary_tree_root

    # Encodes an n-ary tree forest to a binary tree
    def encode_from_forest(self, roots: list[NaryTreeNode | None]) -> TreeNode | None:
        roots = [tree for tree in roots if tree is not None]  # 编码再解码森林后,原顶层森林中的空树会消失
        if len(roots) == 0:
            return None
        binary_tree_roots: list[TreeNode] = [self.encode(x) for x in roots]
        for i in range(len(binary_tree_roots)-2, -1, -1):
            binary_tree_roots[i].right = binary_tree_roots[i+1]
        return binary_tree_roots[0]

    # Decodes your binary tree to an n-ary tree forest
    def decode_to_forest(self, root: TreeNode | None) -> list[NaryTreeNode]:
        if root is None:
            return []
        siblings: list[NaryTreeNode] = []
        pointer: TreeNode | None = root
        while pointer is not None:
            pointer_ = pointer
            pointer = pointer.right
            pointer_.right = None
            siblings.append(self.decode(pointer_))
        return siblings
