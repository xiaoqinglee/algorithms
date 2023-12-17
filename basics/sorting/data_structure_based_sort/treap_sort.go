package data_structure_based_sort

import (
	. "github.com/xiaoqinglee/algorithms/basics/data_structure"
	"math/rand"
	"time"
)

func TreapSort(nums []int) []int {

	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(nums), func(i, j int) {
		nums[i], nums[j] = nums[j], nums[i]
	})

	if len(nums) == 0 {
		return nums
	}

	var container []int

	var root *FHQTreap[int, int]
	for _, num := range nums {
		if val, _, ok := root.GetByKey(num); ok {
			root = root.Insert(num, val+1)
		} else {
			root = root.Insert(num, 1)
		}
	}

	var traverse func(tree *FHQTreap[int, int])
	traverse = func(tree *FHQTreap[int, int]) {
		if tree == nil {
			return
		}
		traverse(tree.L)
		for i := 1; i <= tree.Val; i += 1 {
			container = append(container, tree.Key)
		}
		traverse(tree.R)
	}

	traverse(root)

	return container
}
