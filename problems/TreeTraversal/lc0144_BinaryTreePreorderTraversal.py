from pkg.data_structure import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # root is not None 代表正在进行由上到下遍历并让元素入栈的过程。
    # root is None 代表正在进行由下到上回退并让元素出栈的过程。
    # root由非None变为None，我们只好判断stack是否为空，尝试从stack中pop数据，进行由下到上回退的过程。

    # 前序和中序遍历都是: 父母入栈 -> 左子树入栈 -> 左子树出栈 -> 父母出栈 -> 右子树入栈 -> 右子树出栈
    # 所以
    # 对于先序遍历，node入栈时打印node的value。
    # 对于中序遍历，node出栈时打印node的value。

    # 后序遍历部分节点需要将node入栈两次

    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result: list[int] = []
        if TreeNode is None:
            return result
        stack: list[TreeNode] = []
        while (root is not None) or (len(stack) > 0):
            while root is not None:
                result.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return result

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result: list[int] = []
        if TreeNode is None:
            return result
        stack: list[TreeNode] = []
        while (root is not None) or (len(stack) > 0):
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result: list[int] = []
        if TreeNode is None:
            return result
        stack: list[TreeNode] = []
        last_printed_node: TreeNode | None = None
        while (root is not None) or (len(stack) > 0):
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.right is None:  # 无右子树，故直接打印node，不必二次入栈了。
                result.append(root.val)
                last_printed_node = root
                root = None
            else:  # 有右子树
                if last_printed_node == root.right:  # 右子树已打印完毕，由此可得该出栈元素是第二次出栈。
                    result.append(root.val)
                    last_printed_node = root
                    root = None
                else:  # 右子树还没有打印，所以该node需要第二次入栈，等待右子树打印完毕后该node出栈并打印。
                    stack.append(root)
                    root = root.right
        return result
