package LinkedList

import . "github.com/xiaoqinglee/algorithms/pkg"

// https://leetcode.cn/problems/reverse-linked-list
func reverseList(head *ListNode) *ListNode {
	var newListHead *ListNode
	for {
		if head == nil {
			return newListHead
		}

		newHead := head.Next

		head.Next = newListHead
		newListHead = head

		head = newHead
	}
}
