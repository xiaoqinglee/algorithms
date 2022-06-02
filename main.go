package main

import (
	"fmt"
)

func main() {
	//nums := []int{2, 7, 11, 15}
	//target := 9
	//fmt.Printf("%v\n", problems.TwoSum(nums, target))

	//<nil>
	//true
	//{}
	//true
	//[]
	//true
	//[42]
	var p *string
	var s struct{}
	var slice []int
	fmt.Printf("%v\n", p)
	fmt.Printf("%v\n", p == nil)
	fmt.Printf("%v\n", s)
	fmt.Printf("%v\n", s == struct{}{})
	fmt.Printf("%v\n", slice)
	fmt.Printf("%v\n", len(slice) == 0)
	slice = append(slice, 42)
	fmt.Printf("%v\n", slice)

}
