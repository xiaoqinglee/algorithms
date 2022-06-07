package problems

func calculate(s string) int {

	digitSet := make(map[rune]struct{}, 10)
	for _, digit := range "0123456789" {
		digitSet[digit] = struct{}{}
	}
	var operationStack []rune
	var integerStack []int

	hasEqualOrLessPriorityThan := func(operation1, operation2 rune) bool {
		if (operation1 == '+' || operation1 == '-') ||
			(operation1 == '*' || operation1 == '/') && (operation2 == '*' || operation2 == '/') {
			return true
		}
		return false
	}

	compute := func() {
		left := integerStack[len(integerStack)-2]
		right := integerStack[len(integerStack)-1]
		integerStack = integerStack[:len(integerStack)-2]
		var newOperator int
		operation := operationStack[len(operationStack)-1]
		operationStack = operationStack[:len(operationStack)-1]
		if operation == '+' {
			newOperator = left + right
		} else if operation == '-' {
			newOperator = left - right
		} else if operation == '*' {
			newOperator = left * right
		} else if operation == '/' {
			newOperator = left / right
		}
		integerStack = append(integerStack, newOperator)
	}

	currentNum := 0
	for _, char := range s {
		if char == ' ' {
			continue
		}
		if _, ok := digitSet[char]; ok {
			currentNum *= 10
			currentNum += int(char) - int('0')
		} else {
			integerStack = append(integerStack, currentNum)
			currentNum = 0

			for len(operationStack) > 0 &&
				hasEqualOrLessPriorityThan(char, operationStack[len(operationStack)-1]) {
				compute()
			}
			operationStack = append(operationStack, char)
		}
	}
	integerStack = append(integerStack, currentNum)
	currentNum = 0

	for len(integerStack) != 1 {
		compute()
	}
	return integerStack[0]
}
