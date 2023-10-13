package BinarySearch

import (
	"math"
)

// https://leetcode.cn/problems/sqrtx
func mySqrt(x int) int {

	isRootFloor := func(rootFloor int) bool {
		if rootFloor == math.MaxInt32 { //避免下面的计算发生溢出
			panic("unexpected")
		}
		return rootFloor*rootFloor <= x && x < (rootFloor+1)*(rootFloor+1)
	}
	isRootCeiling := func(rootCeiling int) bool {
		if rootCeiling == 0 { //避免下面的计算出现负数
			return x == 0
		}
		return (rootCeiling-1)*(rootCeiling-1) < x && x <= rootCeiling*rootCeiling
	}
	lo := 0
	hi := math.MaxInt32
	// rootCeiling 在闭区间区间[lo..hi]中, 下面的 for 循环求 rootCeiling
	for {
		if lo == hi {
			break
		}
		rootCeiling := (lo + hi) / 2
		if x <= rootCeiling*rootCeiling {
			hi = rootCeiling
		} else {
			lo = rootCeiling + 1
		}
	}
	rootCeiling := lo
	if !isRootCeiling(rootCeiling) {
		panic("unexpected")
	}
	if isRootFloor(rootCeiling) {
		return rootCeiling
	} else if isRootFloor(rootCeiling - 1) {
		return rootCeiling - 1
	} else {
		panic("unexpected")
	}
}
