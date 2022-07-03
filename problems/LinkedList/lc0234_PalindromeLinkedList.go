package LinkedList

import "github.com/xiaoqinglee/algorithms/pkg"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *pkg.ListNode) bool {
	pointer := head
	var nodes []*pkg.ListNode
	for pointer != nil {
		nodes = append(nodes, pointer)
		pointer = pointer.Next
	}
	pointer = head
	for len(nodes) > 0 {
		top := nodes[len(nodes)-1]

		if top.Val != pointer.Val {
			return false
		}
		nodes = nodes[:len(nodes)-1]
		pointer = pointer.Next
	}
	return true
}
