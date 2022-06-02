package problems

func BinarySearch(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}
	leftIndex := 0
	rightIndex := len(nums) - 1
	for {
		if rightIndex < leftIndex {
			return -1
		}
		midIndex := (leftIndex + rightIndex) / 2
		if nums[midIndex] == target {
			return midIndex
		} else if nums[midIndex] > target {
			rightIndex = midIndex - 1
		} else if nums[midIndex] < target {
			leftIndex = midIndex + 1
		}
	}
}
