package Sorting

import "sort"

func nextPermutation(nums []int) {

	//  1 2 3 4 6 5 3 2 -> 1 2 3 5 2 3 4 6

	//          6
	//            5
	//        4
	//      3       3
	//    2           2
	//  1
	//  1 2 3 4 6 5 3 2
	//        -   -

	//                6
	//        5
	//              4
	//      3     3
	//    2     2
	//  1
	//  1 2 3 5 2 3 4 6
	//        -

	//n = len(nums)-1
	//从右到左遍历数组，找到第一个元素的位置nums[i]，要求nums[i]的右侧非空数组nums[i+1..n-1]内存在比元素nums[i]值更大的元素。
	//(也即自右到左第一个使得nums[i]<nums[i+1]成立的i)
	//找出该右侧非空数组内所有比元素nums[i]大的元素集合中值最小的那个元素nums[j]
	//在数组[i..n-1]内进行如下操作：
	//	nums[i],nums[j] = nums[j],nums[i]
	//  升序排列nums[i+1..n-1]

	if len(nums) <= 1 {
		return
	}
	//找i
	i := len(nums) - 2
	for i >= 0 {
		if nums[i] < nums[i+1] {
			break
		}
		i -= 1
	}
	if i == -1 { // 没有找到i，nums数组是非递增的
		leftPointer := 0
		rightPointer := len(nums) - 1
		for leftPointer < rightPointer {
			nums[leftPointer], nums[rightPointer] = nums[rightPointer], nums[leftPointer]
			leftPointer += 1
			rightPointer -= 1
		}
	} else { // 找到了i
		// 找j
		j := i + 1
		for jCandidate := i + 1; jCandidate < len(nums); jCandidate++ {
			if nums[jCandidate] > nums[i] && nums[jCandidate] < nums[j] {
				j = jCandidate
			}
		}
		nums[i], nums[j] = nums[j], nums[i]
		sort.Ints(nums[i+1:])
	}
}
