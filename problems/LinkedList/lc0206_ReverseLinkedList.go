package LinkedList

import . "github.com/xiaoqinglee/algorithm/pkg"

func ReverseLinkedList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	var newListHead *ListNode
	for {
		newHead := head.Next

		head.Next = newListHead
		newListHead = head

		head = newHead
		if head == nil {
			break
		}
	}
	return newListHead
}
