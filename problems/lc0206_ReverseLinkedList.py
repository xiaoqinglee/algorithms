from pkg.data_structure import ListNode


def reverse_linked_list(head: ListNode | None) -> ListNode | None:
	if head is None:
		return head

	new_list_head: ListNode | None = None
	while True:
		new_head = head.next

		head.next = new_list_head
		new_list_head = head

		head = new_head
		if head is None:
			break

	return new_list_head
