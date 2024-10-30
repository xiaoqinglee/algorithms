package LinkedList

import . "github.com/xiaoqinglee/algorithms/pkg"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// https://leetcode.cn/problems/palindrome-linked-list
func isPalindrome(head *ListNode) bool {
	pointer := head
	var nodes []*ListNode
	for pointer != nil {
		nodes = append(nodes, pointer)
		pointer = pointer.Next
	}

	for len(nodes) > 0 {

		if len(nodes) == 1 {
			return true
		}

		bottom := nodes[0]
		top := nodes[len(nodes)-1]

		if bottom.Val != top.Val {
			return false
		}
		nodes = nodes[1 : len(nodes)-1]
	}
	return true
}
