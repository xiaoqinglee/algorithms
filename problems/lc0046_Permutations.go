package problems

func Permute(nums []int) [][]int {
	result := make([][]int, 0)

	swapTwoElementByIndex := func(pList *[]int, i int, j int) {
		(*pList)[i], (*pList)[j] = (*pList)[j], (*pList)[i]
	}

	var backTrace func(fixedFirstNElement int)
	backTrace = func(fixedFirstNElement int) {
		if fixedFirstNElement == len(nums) {
			oneCombination := make([]int, len(nums), len(nums))
			copy(oneCombination, nums)
			result = append(result, oneCombination)
		}
		for i := fixedFirstNElement; i < len(nums); i++ {
			swapTwoElementByIndex(&nums, fixedFirstNElement, i)
			backTrace(fixedFirstNElement + 1)
			swapTwoElementByIndex(&nums, fixedFirstNElement, i)
		}
	}

	backTrace(0)
	return result
}
