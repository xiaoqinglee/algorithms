package LinkedList

import "github.com/xiaoqinglee/algorithms/pkg"

func RemoveNthFromEnd(head *pkg.ListNode, n int) *pkg.ListNode {
	if head == nil || n <= 0 {
		panic("Invalid Input head or n")
	}

	dummyHead := &pkg.ListNode{
		Val:  0,
		Next: head,
	}

	isLastNode := func(node *pkg.ListNode) bool {
		return node != nil && node.Next == nil
	}

	firstPointer := dummyHead
	for i := 1; i <= n; i++ {
		if isLastNode(firstPointer) {
			panic("Invalid Input head")
		}
		firstPointer = firstPointer.Next
	}
	secondPointer := dummyHead

	for {
		if isLastNode(firstPointer) {
			break
		}
		firstPointer = firstPointer.Next
		secondPointer = secondPointer.Next
	}
	secondPointer.Next = secondPointer.Next.Next
	return dummyHead.Next

}
