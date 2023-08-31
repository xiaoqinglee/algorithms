package Math

// https://leetcode.cn/problems/power-of-three
func isPowerOfThree(n int) bool {
	for {
		if n == 1 {
			return true
		}
		if !(n > 0 && n%3 == 0) {
			return false
		}
		n = n / 3
	}
}
