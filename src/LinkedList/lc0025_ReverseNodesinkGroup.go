package LinkedList

import . "github.com/xiaoqinglee/algorithms/pkg"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// https://leetcode.cn/problems/reverse-nodes-in-k-group
func reverseKGroup(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}
	if k <= 0 {
		panic("Invalid Input k")
	}
	newListDummyHead := &ListNode{Val: -1, Next: nil}
	newListLastNode := newListDummyHead

	var fixSizedStack []*ListNode

	for head != nil {
		newHead := head.Next

		head.Next = nil // 将节点变为游离态，然后再放入容器中，是良好的习惯
		fixSizedStack = append(fixSizedStack, head)

		if len(fixSizedStack) == k {
			for len(fixSizedStack) > 0 {
				node := fixSizedStack[len(fixSizedStack)-1]
				fixSizedStack = fixSizedStack[:len(fixSizedStack)-1]
				newListLastNode.Next = node
				newListLastNode = newListLastNode.Next
			}
		}

		head = newHead
	}
	//如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
	for _, node := range fixSizedStack {
		newListLastNode.Next = node
		newListLastNode = newListLastNode.Next
	}
	return newListDummyHead.Next
}
