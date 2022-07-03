package Sorting

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

func MergeSort(nums []int) []int {

	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(nums), func(i, j int) {
		nums[i], nums[j] = nums[j], nums[i]
	})

	if len(nums) == 0 {
		return nums
	}

	container := make([]int, len(nums), len(nums))

	merge := func(leftIndex, midIndex, rightIndex int) {
		copy(container[leftIndex:rightIndex+1], nums[leftIndex:rightIndex+1])
		leftPointer, rightPointer, mergingPointer := leftIndex, midIndex+1, leftIndex

		for leftPointer <= midIndex && rightPointer <= rightIndex {
			if container[leftPointer] <= container[rightPointer] {
				nums[mergingPointer] = container[leftPointer]
				leftPointer += 1
			} else {
				nums[mergingPointer] = container[rightPointer]
				rightPointer += 1
			}
			mergingPointer += 1
		}
		for leftPointer <= midIndex {
			nums[mergingPointer] = container[leftPointer]
			leftPointer += 1
			mergingPointer += 1
		}
		for rightPointer <= rightIndex {
			nums[mergingPointer] = container[rightPointer]
			rightPointer += 1
			mergingPointer += 1
		}
	}

	var sort_ func(int, int)
	sort_ = func(leftIndex, rightIndex int) {
		if leftIndex >= rightIndex {
			return
		}
		midIndex := (leftIndex + rightIndex) / 2
		sort_(leftIndex, midIndex)
		sort_(midIndex+1, rightIndex)
		merge(leftIndex, midIndex, rightIndex)
	}
	sort_(0, len(nums)-1)
	return nums
}
