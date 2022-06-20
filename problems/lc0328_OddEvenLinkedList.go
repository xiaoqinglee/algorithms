package problems

import "github.com/xiaoqinglee/algorithm/pkg"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func oddEvenList(head *pkg.ListNode) *pkg.ListNode {
	if head == nil {
		return head
	}
	l1DummyHead := new(pkg.ListNode)
	l1Tail := l1DummyHead
	l2DummyHead := new(pkg.ListNode)
	l2Tail := l2DummyHead

	for head != nil {
		newHead := head.Next
		head.Next = nil
		l1Tail.Next = head
		l1Tail = l1Tail.Next
		head = newHead

		if head == nil {
			break
		}
		newHead = head.Next
		head.Next = nil
		l2Tail.Next = head
		l2Tail = l2Tail.Next
		head = newHead
	}
	l1Tail.Next = l2DummyHead.Next
	return l1DummyHead.Next
}
