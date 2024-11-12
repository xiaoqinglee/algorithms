package TwoPointers

// https://leetcode.cn/problems/remove-element
func removeElement(nums []int, val int) int {
	for i := 0; i <= len(nums)-1; {
		if nums[i] == val {
			nums[i] = nums[len(nums)-1]
			nums = nums[:len(nums)-1]
		} else {
			i += 1
		}
	}
	return len(nums)
}
