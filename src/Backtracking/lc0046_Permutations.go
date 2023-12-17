package Backtracking

// https://leetcode.cn/problems/permutations/
func permute(nums []int) [][]int {
	result := make([][]int, 0)

	swapTwoElementByIndex := func(pList *[]int, i int, j int) {
		(*pList)[i], (*pList)[j] = (*pList)[j], (*pList)[i]
	}

	var backTrace func(fixedFirstNElement int)
	backTrace = func(fixedFirstNElement int) {
		if fixedFirstNElement == len(nums) {
			oneCombination := make([]int, len(nums), len(nums))
			copy(oneCombination, nums)
			//作为对比，在 elixir 中：
			//匿名函数可以捕获外部值成为闭包，但是无法递归调用自己.
			//有名函数可以递归调用自己，但是无法捕获外部值成为闭包.
			//see:
			//Learn Functional Programming with Elixir by Ulisses Almeida
			//Using Recursion with Anonymous Functions
			//
			//需要注意，elixir 捕获的总是值（是不可变的），而 golang 捕获的是变量（是可变的）。
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
