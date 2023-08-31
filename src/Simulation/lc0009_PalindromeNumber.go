package Simulation

// https://leetcode.cn/problems/palindrome-number
func isPalindrome(x int) bool {
	if x < 0 || x%10 == 0 && x != 0 {
		return false
	}
	reversedNumber := 0
	for {
		if reversedNumber == x/10 || reversedNumber == x {
			return true
		} else if reversedNumber > x {
			return false
		}
		reversedNumber = reversedNumber*10 + x%10
		x = x / 10
	}
}
