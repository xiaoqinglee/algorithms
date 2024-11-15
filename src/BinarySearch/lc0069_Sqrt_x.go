package BinarySearch

import (
	"math"
)

// https://leetcode.cn/problems/sqrtx
func mySqrt(x int) int {

	equalToRootFloor := func(rootFloor int) bool {
		if rootFloor == math.MaxInt32 { //避免下面的计算发生溢出
			panic("unexpected")
		}
		return rootFloor*rootFloor <= x && x < (rootFloor+1)*(rootFloor+1)
	}
	greaterThanRootFloor := func(candidate int) bool {
		if candidate == math.MaxInt32 { //避免下面的计算发生溢出
			panic("unexpected")
		}
		return x < candidate*candidate
	}

	lo := 0
	hi := math.MaxInt32
	// 在闭区间 [lo..hi] 中寻找第一个满足某个条件的整数，数组的右半段都满足这个条件(至少hi满足)
	for {
		if lo == hi {
			break
		}
		mid := (lo + hi) / 2
		if greaterThanRootFloor(mid) || equalToRootFloor(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
