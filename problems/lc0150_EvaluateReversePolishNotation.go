package problems

import (
	"strconv"
)

func evalRPN(tokens []string) int {
	var operatorStack []int
	operationSet := make(map[string]struct{})
	for _, token := range "+-*/" {
		operationSet[string(token)] = struct{}{}
	}
	for _, token := range tokens {
		if _, ok := operationSet[token]; !ok {
			tokenInInt, _ := strconv.Atoi(token)
			operatorStack = append(operatorStack, tokenInInt)
		} else {
			left := operatorStack[len(operatorStack)-2]
			right := operatorStack[len(operatorStack)-1]
			operatorStack = operatorStack[:len(operatorStack)-2]
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
			operatorStack = append(operatorStack, newOperator)
		}
	}
	return operatorStack[0]
}
