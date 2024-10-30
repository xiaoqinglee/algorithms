# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pkg.data_structure import ListNode


# https://leetcode.cn/problems/reorder-list
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # head 的值没有发生变化，只改变了各个node中next指针的值
        if head is None:
            return head
        array: list[ListNode] = []
        pointer = head
        while pointer is not None:
            array.append(pointer)
            pointer = pointer.next
        front_pointer = 0
        back_pointer = len(array) - 1
        dummy_head = ListNode(val=0, next=None)
        new_list_last_node = dummy_head
        while True:
            if front_pointer > back_pointer:
                break
            elif front_pointer == back_pointer:
                new_list_last_node.next = array[front_pointer]
                new_list_last_node = new_list_last_node.next
                new_list_last_node.next = None
            else:  # front_pointer < back_pointer
                new_list_last_node.next = array[front_pointer]
                new_list_last_node = new_list_last_node.next
                new_list_last_node.next = array[back_pointer]
                new_list_last_node = new_list_last_node.next
                new_list_last_node.next = None
            front_pointer += 1
            back_pointer -= 1
