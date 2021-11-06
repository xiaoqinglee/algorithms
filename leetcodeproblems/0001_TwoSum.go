package leetcodeproblems

func TwoSum(nums []int, target int) []int {
	hashtable := make(map[int]int, len(nums))
	for i, num := range nums {
		if index, ok := hashtable[target-num]; ok {
			return []int{index, i}
		}
		hashtable[num] = i
	}
	return []int{}
}
