from pkg.data_structure import ListNode


# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
def remove_nth_node_from_end_of_list(head: ListNode | None, n: int) -> ListNode | None:
    if head is None or n <= 0:
        raise "Invalid Input head and n"

    is_last_node = lambda node: (node is not None) and node.next is None
    dummy_head = ListNode(val=0, next=head)

    # pointer 指向非None的Node
    first_pointer = dummy_head
    for i in range(n):
        if is_last_node(first_pointer):
            raise "Invalid Input head"
        first_pointer = first_pointer.next
    second_pointer = dummy_head

    while True:
        if is_last_node(first_pointer):
            break
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    second_pointer.next = second_pointer.next.next
    return dummy_head.next

