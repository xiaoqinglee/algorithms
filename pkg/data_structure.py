class ListNode:
    def __init__(self, val, next=None):
        self.val: int = val
        self.next: ListNode | None = next


class DoublyLinkedListNode:
    def __init__(self, val, prev=None, next=None):
        self.val: int = val
        self.prev: DoublyLinkedListNode | None = prev
        self.next: DoublyLinkedListNode | None = next


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right
