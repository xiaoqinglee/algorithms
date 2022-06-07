package problems

import (
	"strconv"
)

func evalRPN(tokens []string) int {
	var operators []int
	operationSet := make(map[string]struct{})
	for _, token := range "+-*/" {
		operationSet[string(token)] = struct{}{}
	}
	for _, token := range tokens {
		if _, ok := operationSet[token]; !ok {
			tokenInInt, _ := strconv.Atoi(token)
			operators = append(operators, tokenInInt)
			continue
		}
		left := operators[len(operators)-2]
		right := operators[len(operators)-1]
		operators = operators[:len(operators)-2]
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
		operators = append(operators, newOperator)
	}
	return operators[0]
}
