package problems

import (
	"math/rand"
	"time"
)

func QuickSort(nums []int) []int {

	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(nums), func(i, j int) {
		nums[i], nums[j] = nums[j], nums[i]
	})

	if len(nums) == 0 {
		return nums
	}

	partition := func(leftIndex, rightIndex int) (midIndex int) {
		leftPointer, rightPointer := leftIndex, rightIndex

		toCompareWith := nums[leftPointer]

		for {
			for leftPointer < rightPointer && toCompareWith <= nums[rightPointer] {
				rightPointer -= 1
			}
			if leftPointer == rightPointer {
				break
			}
			nums[leftPointer] = nums[rightPointer]
			leftPointer += 1

			for leftPointer < rightPointer && nums[leftPointer] < toCompareWith {
				leftPointer += 1
			}
			if leftPointer == rightPointer {
				break
			}
			nums[rightPointer] = nums[leftPointer]
			rightPointer -= 1
		}
		nums[leftPointer] = toCompareWith
		return leftPointer
	}

	var sort_ func(int, int)
	sort_ = func(leftIndex, rightIndex int) {
		if leftIndex >= rightIndex {
			return
		}
		midIndex := partition(leftIndex, rightIndex)
		sort_(leftIndex, midIndex-1)
		sort_(midIndex+1, rightIndex)

	}
	sort_(0, len(nums)-1)
	return nums
}
