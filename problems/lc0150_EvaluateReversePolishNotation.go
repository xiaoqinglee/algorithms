package problems

import (
	"strconv"
)

func evalRPN(tokens []string) int {
	var nums []int
	operationSet := make(map[string]struct{})
	for _, token := range "+-*/" {
		operationSet[string(token)] = struct{}{}
	}
	for _, token := range tokens {
		if _, ok := operationSet[token]; !ok {
			tokenInInt, _ := strconv.Atoi(token)
			nums = append(nums, tokenInInt)
		} else {
			left := nums[len(nums)-2]
			right := nums[len(nums)-1]
			nums = nums[:len(nums)-2]
			var newOperator int
			switch token {
			case "+":
				newOperator = left + right
			case "-":
				newOperator = left - right
			case "*":
				newOperator = left * right
			case "/":
				newOperator = left / right
			}
			nums = append(nums, newOperator)
		}
	}
	return nums[0]
}
