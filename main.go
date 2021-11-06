package main

import (
	"fmt"
	"github.com/XiaoqingLee/LeetCodeProblems/leetcodeproblems"
	"github.com/XiaoqingLee/LeetCodeProblems/pkg"
)

func main() {
	l1 := pkg.SliceToListNode([]int{2, 4, 5})
	l2 := pkg.SliceToListNode([]int{5, 6, 4})
	l3 := leetcodeproblems.AddTwoNumbers(l1, l2)
	fmt.Printf("%#v", l3.ToSlice())

}
