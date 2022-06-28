class ListNode:
    def __init__(self, val, next=None):
        self.val: int = val
        self.next: ListNode | None = next


class DoubleLinkedListNode:
    def __init__(self, val, prev=None, next=None):
        self.val: int = val
        self.prev: DoubleLinkedListNode | None = prev
        self.next: DoubleLinkedListNode | None = next


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right
