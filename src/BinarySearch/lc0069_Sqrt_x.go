package BinarySearch

import "math"

// https://leetcode.cn/problems/sqrtx
func mySqrt(x int) int {
	foundIt := func(root int) bool {
		return root*root <= x && x < (root+1)*(root+1)
	}
	leftCursor := 0
	rightCursor := math.MaxInt32
	// 答案在区间[leftCursor..rightCursor]中，只要区间元素个数不为零，就需要继续计算
	for leftCursor <= rightCursor {
		mid := (leftCursor + rightCursor) / 2
		if foundIt(mid) {
			return mid
		} else if mid*mid < x {
			leftCursor = mid + 1
		} else if mid*mid > x {
			rightCursor = mid - 1
		}
	}
	return -1 //只是为了迁就语法，这里根本得不到执行
}
