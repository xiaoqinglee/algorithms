package TwoPointers

func moveZeroes(nums []int) {
	indexToReadFrom, indexToWriteTo := 0, 0
	for indexToReadFrom <= len(nums)-1 {
		if nums[indexToReadFrom] != 0 {
			nums[indexToWriteTo] = nums[indexToReadFrom]
			indexToWriteTo += 1
		}
		indexToReadFrom += 1
	}
	for indexToWriteTo <= len(nums)-1 {
		nums[indexToWriteTo] = 0
		indexToWriteTo += 1
	}
}
