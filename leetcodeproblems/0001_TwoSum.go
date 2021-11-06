package leetcodeproblems

func TwoSum(nums []int, target int) []int {
	mapValueToIndex := make(map[int]int, len(nums))
	for i, num := range nums {
		if index, ok := mapValueToIndex[target-num]; ok {
			return []int{index, i}
		}
		mapValueToIndex[num] = i
	}
	return []int{}
}
