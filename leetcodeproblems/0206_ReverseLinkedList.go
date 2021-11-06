package leetcodeproblems

import . "github.com/XiaoqingLee/LeetCodeProblems/pkg"

func ReverseList(pHead *ListNode) *ListNode {
	var pNewListHead *ListNode
	var pTail *ListNode
	for {
		if pHead == nil {
			break
		}
		//第一步
		pTail = pHead.Next
		//第三步
		pHead.Next = pNewListHead
		pNewListHead = pHead
		//第二步
		pHead = pTail
	}
	return pNewListHead
}
