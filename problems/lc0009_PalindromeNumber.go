package problems

func PalindromeNumber(x int) bool {

	//如果一个int32变量是回文数, 那么他的reversed形式和他本身相等, 所以他的reversed形式肯定不会溢出
	//所以如果溢出肯定不是回文数

	if x == 0 {
		return true
	} else if x < 0 {
		return false
	}
	reversed := ReverseInteger(x)
	if reversed == 0 { //溢出了
		return false
	} else if reversed != x {
		return false
	}
	return true
}

func PalindromeNumber2(x int) bool {
	// 特殊情况：
	// 如上所述，当 x < 0 时，x 不是回文数。
	// 同样地，如果数字的最后一位是 0，为了使该数字为回文，
	// 则其第一位数字也应该是 0
	// 只有 0 满足这一属性
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}

	reversed := 0
	for x > reversed {
		reversed = reversed*10 + x%10
		x /= 10
	}

	// 当数字长度为奇数时，我们可以通过 reversed/10 去除处于中位的数字。
	return x == reversed || x == reversed/10
}
