import heapq

from pypkg.datatype import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 自顶向下归并
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        # 题目要求 K >= 0
        if len(lists) == 0:
            return None

        def merge_two_linked_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
            l3_dummy_head = ListNode(val=0, next=None)
            l3_last_node = l3_dummy_head
            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    l3_last_node.next = l1
                    l3_last_node = l3_last_node.next
                    l1 = l1.next
                else:
                    l3_last_node.next = l2
                    l3_last_node = l3_last_node.next
                    l2 = l2.next
            if l1 is not None:
                l3_last_node.next = l1
            elif l2 is not None:
                l3_last_node.next = l2
            return l3_dummy_head.next

        def merge(left_index: int, right_index: int) -> ListNode | None: # 左右边界都包含
            if left_index == right_index:  # 1个元素
                return lists[left_index]
            elif right_index - left_index == 1:  # 2个元素
                return merge_two_linked_lists(lists[left_index], lists[right_index])
            elif right_index - left_index >= 2:  # 3或3个以上元素
                mid_index = (left_index + right_index) // 2
                left_half = merge(left_index, mid_index)
                right_half = merge(mid_index + 1, right_index)
                return merge_two_linked_lists(left_half, right_half)

        return merge(0, len(lists) - 1)

    # 堆排序
    def mergeKLists2(self, lists: list[ListNode | None]) -> ListNode | None:

        # 题目要求 K >= 0
        if len(lists) == 0:
            return None

        new_list_dummy_head = ListNode(val=0, next=None)
        new_list_tail = new_list_dummy_head

        # python heapq 算法包使用最小堆逻辑
        # tuple(node_val, from_which_linked_list]
        heap: list[tuple[int, int]] = []

        for index, node in enumerate(lists):
            if node is not None:
                heap.append((node.val, index))

        heapq.heapify(heap)
        while len(heap) > 0:

            _, from_which_linked_list = heap[0]
            heapq.heappop(heap)

            node = lists[from_which_linked_list]
            lists[from_which_linked_list] = node.next
            node.next = None

            new_list_tail.next = node
            new_list_tail = new_list_tail.next

            if lists[from_which_linked_list] is not None:
                heapq.heappush(heap, (lists[from_which_linked_list].val, from_which_linked_list))

        return new_list_dummy_head.next
