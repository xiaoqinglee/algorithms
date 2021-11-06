package pkg

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func (l *ListNode) String() string {
	return fmt.Sprintf("%v", l.ToSlice())
}

func (l *ListNode) ToSlice() []int {
	var slice []int
	curr := l
	for {
		if curr == nil {
			break
		}
		slice = append(slice, curr.Val)
		curr = curr.Next
	}
	return slice
}
func SliceToListNode(slice []int) *ListNode {
	var l *ListNode
	var lLastNode *ListNode
	for _, value := range slice {
		lNewNode := &ListNode{
			Val:  value,
			Next: nil,
		}
		if l == nil {
			l = lNewNode
			lLastNode = lNewNode
		} else {
			lLastNode.Next = lNewNode
			lLastNode = lNewNode
		}
	}
	return l
}
