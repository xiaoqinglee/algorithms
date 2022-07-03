package TwoPointers

func removeElement(nums []int, val int) int {
	length := len(nums)
	i := 0
	for i < length {
		if nums[i] == val {
			nums[i] = nums[length-1]
			length -= 1
		} else {
			i += 1
		}
	}
	return length
}
