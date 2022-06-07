package problems

func calculate_2(s string) int {

	//面试题 16.26. 计算器
	//https://leetcode.cn/problems/calculator-lcci/
	// 简单题，运算符有+-*/这4种，数字可以超过一位，输入中可能包含空格

	digitSet := make(map[rune]struct{}, 10)
	for _, digit := range "0123456789" {
		digitSet[digit] = struct{}{}
	}
	var operations []rune
	var nums []int

	hasEqualOrLessPriorityThan := func(operation1, operation2 rune) bool {
		if (operation1 == '+' || operation1 == '-') ||
			(operation1 == '*' || operation1 == '/') && (operation2 == '*' || operation2 == '/') {
			return true
		}
		return false
	}

	compute := func() {
		left := nums[len(nums)-2]
		right := nums[len(nums)-1]
		nums = nums[:len(nums)-2]
		var newOperator int
		operation := operations[len(operations)-1]
		operations = operations[:len(operations)-1]
		if operation == '+' {
			newOperator = left + right
		} else if operation == '-' {
			newOperator = left - right
		} else if operation == '*' {
			newOperator = left * right
		} else if operation == '/' {
			newOperator = left / right
		}
		nums = append(nums, newOperator)
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
			nums = append(nums, currentNum)
			currentNum = 0

			for len(operations) > 0 &&
				hasEqualOrLessPriorityThan(char, operations[len(operations)-1]) {
				compute()
			}
			operations = append(operations, char)
		}
	}
	nums = append(nums, currentNum)
	currentNum = 0

	for len(nums) != 1 {
		compute()
	}
	return nums[0]
}

//	227. 基本计算器 II
//	https://leetcode.cn/problems/basic-calculator-ii/
//	同上

//	224. 基本计算器
//	https://leetcode.cn/problems/basic-calculator/
//	s 由数字、'+'、'-'、'('、')' 和 ' ' 组成
//	'+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
//	'-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
//	困难题

//	终极题目：
//	https://leetcode.cn/problems/basic-calculator-ii/solution/shi-yong-shuang-zhan-jie-jue-jiu-ji-biao-c65k/
//	s 由数字、'+'、'-'、'*'、'/'、'('、')' 和 ' ' 组成
//	'+' 可以用作一元运算(例如， "+1" 和 "+(2 + 3)" 有效)
//	'-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 有效)
func calculate_1(s string) int {

	//	终极题目解法：
	//
	//	对于「任何表达式」而言，我们都使用两个栈 nums 和 ops：
	//
	//	nums ： 存放所有的数字
	//	ops ：存放所有的数字以外的操作
	//
	//	然后从前往后做，对遍历到的字符做分情况讨论：
	//
	//	空格 : 跳过
	//	( : 直接加入 ops 中，等待与之匹配的 )
	//	) : 使用现有的 nums 和 ops 进行计算，直到遇到左边最近的一个左括号为止，计算结果放到 nums
	//	数字 : 从当前位置开始继续往后取，将整一个连续数字整体取出，加入 nums
	//	+ - * / ^ % : 需要将操作放入 ops 中。在放入之前先把栈内可以算的都算掉（只有「栈内运算符」比「当前运算符」优先级高/同等，才进行运算），使用现有的 nums 和 ops 进行计算，直到没有操作或者遇到左括号，计算结果放到 nums
	//
	//	一些细节：
	//
	//	由于第一个数可能是负数，为了减少边界判断。一个小技巧是先往 nums 添加一个 0
	//	为防止 () 内出现的首个字符为运算符，将所有的空格去掉，并将 (- 替换为 (0-，(+ 替换为 (0+（当然也可以不进行这样的预处理，将这个处理逻辑放到循环里去做）

	digitSet := make(map[rune]struct{}, 10)
	for _, digit := range "0123456789" {
		digitSet[digit] = struct{}{}
	}
	var operations []rune
	var nums []int

	hasEqualOrLessPriorityThan := func(operation1, operation2 rune) bool {
		if (operation1 == '+' || operation1 == '-') ||
			(operation1 == '*' || operation1 == '/') && (operation2 == '*' || operation2 == '/') {
			return true
		}
		return false
	}

	compute := func() {
		left := nums[len(nums)-2]
		right := nums[len(nums)-1]
		nums = nums[:len(nums)-2]
		var newOperator int
		operation := operations[len(operations)-1]
		operations = operations[:len(operations)-1]
		if operation == '+' {
			newOperator = left + right
		} else if operation == '-' {
			newOperator = left - right
		} else if operation == '*' {
			newOperator = left * right
		} else if operation == '/' {
			newOperator = left / right
		}
		nums = append(nums, newOperator)
	}

	currentNum := 0
	previousCharIsDigit := false
	for i, char := range s {
		if char == ' ' {
			continue
		}
		if _, ok := digitSet[char]; ok {
			currentNum *= 10
			currentNum += int(char) - int('0')
			previousCharIsDigit = true
		} else {

			if previousCharIsDigit {
				nums = append(nums, currentNum)
				currentNum = 0
				previousCharIsDigit = false
			}

			if char == '(' {
				operations = append(operations, char)
			} else if char == ')' {
				for operations[len(operations)-1] != '(' {
					compute()
				}
				operations = operations[:len(operations)-1]
			} else if (char == '+' || char == '-') && (i == 0 || i >= 1 && s[i-1] == '(') { // 一元+-
				nums = append(nums, 0)
				operations = append(operations, char)
			} else { // 二元+-*/
				for len(operations) > 0 &&
					operations[len(operations)-1] != '(' &&
					hasEqualOrLessPriorityThan(char, operations[len(operations)-1]) {
					compute()
				}
				operations = append(operations, char)
			}
		}
	}

	if previousCharIsDigit {
		nums = append(nums, currentNum)
		currentNum = 0
		previousCharIsDigit = false
	}

	for len(nums) != 1 {
		compute()
	}
	return nums[0]
}
