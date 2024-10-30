package LinkedList

import . "github.com/xiaoqinglee/algorithms/pkg"

// https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	var fastPointer, slowPointer, slowPreviousPointer *ListNode = head, head, nil

	fastPointer = head
	for i := 1; i <= n; i++ {
		fastPointer = fastPointer.Next
	}

	for {
		if fastPointer == nil {
			if slowPreviousPointer == nil {
				return slowPointer.Next //删去第一个节点
			} else {
				slowPreviousPointer.Next = slowPointer.Next
				return head
			}
		}
		fastPointer = fastPointer.Next
		slowPreviousPointer = slowPointer
		slowPointer = slowPointer.Next
	}
}
