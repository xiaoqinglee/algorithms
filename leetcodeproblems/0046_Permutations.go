package leetcodeproblems

import "fmt"

func allCombinations_(used, left []int, resultAddress *[][]int) {

	if len(left) == 0 {
		*resultAddress = append(*resultAddress, used)
		return
	}

	for i, v := range left {

		newUsed := make([]int, len(used), cap(used))
		copy(newUsed, used)
		newUsed = append(newUsed, v)

		newLeft := make([]int, len(left), cap(left))
		copy(newLeft, left)
		newLeft = append(newLeft[:i], newLeft[i+1:]...)

		allCombinations_(newUsed, newLeft, resultAddress)
	}
}

func allCombinations(nums []int) [][]int {
	result := [][]int{}
	allCombinations_([]int{}, nums, &result)
	return result
}

func main() {
	nums := []int{0, 1, 2}
	result := allCombinations(nums)
	fmt.Printf("result: %v", result)
}
