package main

import (
	"fmt"
	"github.com/xiaoqinglee/algorithms/basics/sorting/bubble_sort"
	"github.com/xiaoqinglee/algorithms/basics/sorting/insertion_sort"
	"github.com/xiaoqinglee/algorithms/basics/sorting/selection_sort"
)

func main() {
	//s1 := strings.Clone("")
	//s2 := strings.Clone("")
	//spew.Dump(&s1)
	//spew.Dump(&s2)
	//spew.Dump(&s1 == &s2)

	s1 := []int{9, 1, 4, 2, 6, 1}
	s2 := []int{9, 1, 4, 2, 6, 1}

	fmt.Println(s1)
	bubble_sort.BubbleSort(s1)
	fmt.Println(s1)
	copy(s1, s2)

	fmt.Println(s1)
	selection_sort.SelectionSort(s1)
	fmt.Println(s1)
	copy(s1, s2)

	fmt.Println(s1)
	insertion_sort.InsertionSort(s1)
	fmt.Println(s1)
	copy(s1, s2)
}
