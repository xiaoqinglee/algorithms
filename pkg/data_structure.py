class ListNode:
    def __init__(self, val, next=None):
        self.val: int = val
        self.next: ListNode = next


class DoubleLinkedListNode:
    def __init__(self, val, prev=None, next=None):
        self.val: int = val
        self.prev: DoubleLinkedListNode = prev
        self.next: DoubleLinkedListNode = next


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right
