package Simulation

import "math"

// https://leetcode.cn/problems/reverse-integer

// golang
////-98 -7
////-9 -8
////0 -9
////-12 -3
////-1 -2
////0 -1
//fmt.Printf("%v %v\n", -987/10, -987%10)
//fmt.Printf("%v %v\n", -98/10, -98%10)
//fmt.Printf("%v %v\n", -9/10, -9%10)
//fmt.Printf("%v %v\n", -123/10, -123%10)
//fmt.Printf("%v %v\n", -12/10, -12%10)
//fmt.Printf("%v %v\n", -1/10, -1%10)

// python3
//# [[-99, 3], [-10, 2], [-1, 1], [-13, 7], [-2, 8], [-1, 9]]
//    print([
//        [-987 // 10, -987 % 10],
//        [-98 // 10, -98 % 10],
//        [-9 // 10, -9 % 10],
//
//        [-123 // 10, -123 % 10],
//        [-12 // 10, -12 % 10],
//        [-1 // 10, -1 % 10],
//    ])

// 使用golang实现时，只要加了针对负数的溢出判断，处理负数的逻辑和处理正数的逻辑完全一样
func reverse(x int) int {
	rev := 0
	for {
		if x == 0 {
			return rev
		}

		digit := x % 10
		x = x / 10

		if !(math.MinInt32/10 <= rev && rev <= math.MaxInt32/10) {
			return 0
		}
		rev = rev*10 + digit
	}
}
