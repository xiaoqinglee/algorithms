package Math

import "fmt"

// https://leetcode.cn/problems/ugly-number-ii
func nthUglyNumber(n int) {
	fmt.Println(nthUglyNumber1(n))
	fmt.Println(nthUglyNumber2(n))
	fmt.Println(nthUglyNumber3(n))
}

// 递归无优化
func nthUglyNumber1(n int) int {

	var isUglyNumber func(int) bool
	isUglyNumber = func(num int) bool { //要求num>0
		return num == 1 ||
			(num%2 == 0 && isUglyNumber(num/2)) ||
			(num%3 == 0 && isUglyNumber(num/3)) ||
			(num%5 == 0 && isUglyNumber(num/5))
	}

	count := 0
	for i := 1; ; i += 1 {
		if isUglyNumber(i) {
			count += 1
			if count == n {
				return i
			}
		}
	}
}

// 记忆化函数缓存重复子问题结果
func nthUglyNumber2(n int) int {

	isUglyNumberCache := make(map[int]bool)
	var isUglyNumber func(int) bool
	isUglyNumber = func(num int) bool { //要求num>0
		if is, ok := isUglyNumberCache[num]; ok {
			return is
		}
		is := num == 1 ||
			(num%2 == 0 && isUglyNumber(num/2)) ||
			(num%3 == 0 && isUglyNumber(num/3)) ||
			(num%5 == 0 && isUglyNumber(num/5))
		isUglyNumberCache[num] = is
		return is
	}

	count := 0
	for i := 1; ; i += 1 {
		if isUglyNumber(i) {
			count += 1
			if count == n {
				return i
			}
		}
	}
}

// 动态规划按序打表
func nthUglyNumber3(n int) int {

	isUglyNumberCache := make(map[int]bool)
	count := 0
	for i := 1; ; i += 1 { //要求i>0, 因为 0 % k = 0
		is := false
		if i == 1 ||
			(i%2 == 0 && isUglyNumberCache[i/2]) ||
			(i%3 == 0 && isUglyNumberCache[i/3]) ||
			(i%5 == 0 && isUglyNumberCache[i/5]) {
			count += 1
			if count == n {
				return i
			}
			is = true
		}
		isUglyNumberCache[i] = is
	}
}
