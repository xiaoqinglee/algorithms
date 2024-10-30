package LinkedList

import (
	. "github.com/xiaoqinglee/algorithms/pkg"
)

// https://leetcode.cn/problems/add-two-numbers
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var l3 *ListNode
	var l3LastNode *ListNode
	var l1NodeValue int
	var l2NodeValue int
	var addNAtHigherDigit int
	for {
		if l1 == nil && l2 == nil && addNAtHigherDigit == 0 {
			break
		}
		if l1 == nil {
			l1NodeValue = 0
		} else {
			l1NodeValue = l1.Val
			l1 = l1.Next
		}
		if l2 == nil {
			l2NodeValue = 0
		} else {
			l2NodeValue = l2.Val
			l2 = l2.Next
		}
		nodeSum := l1NodeValue + l2NodeValue + addNAtHigherDigit
		if nodeSum >= 10 {
			addNAtHigherDigit = nodeSum / 10
			nodeSum = nodeSum % 10
		} else {
			addNAtHigherDigit = 0
		}
		l3NewNode := &ListNode{
			Val: nodeSum,
		}
		if l3 == nil {
			l3 = l3NewNode
			l3LastNode = l3NewNode
		} else {
			l3LastNode.Next = l3NewNode
			l3LastNode = l3NewNode
		}
	}
	return l3
}
