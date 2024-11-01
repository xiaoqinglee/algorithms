package SlidingWindow

import (
	"math"
)

// https://leetcode.cn/problems/minimum-window-substring

//参考lc0003和lc0076 滑动窗口总结
//滑动窗口移动右指针会让窗口扩张，移动左指针会让窗口收缩，那么什么时候移动右指针，什么时候移动左指针呢？
//
//求最小窗口：
//	比如lc0076
//	最小值在收缩的过程中获得。
//	扩张过程：收劲，见好就收。遇到第一个能让收缩过程继续下去的情况（即让窗口满足条件的情况）后立即停下来，转向收缩过程。
//	收缩过程：使劲，逼到极限。遇到第一个让窗口满足条件的地方不会停下来，因为移动到下一个位置可能仍然满足条件，
//		从而获得一个更小的窗口，直到不满足条件从而转向扩张过程。【每次收缩后比较并记录下最小窗口。】
//
//求最大窗口：
//	比如lc0003
//	最大值在窗口扩张的过程中获得。
//	扩张过程：使劲，逼到极限。遇到第一个让窗口满足条件的地方不会停下来，因为移动到下一个位置可能仍然满足条件，
//		从而获得一个更大的窗口，直到不满足条件从而转向收缩过程。【每次扩张后比较并记录下最大窗口。】
//	收缩过程：收劲，见好就收。遇到第一个能让扩张过程继续下去的情况（即让窗口满足条件的情况）后立即停下来，转向扩张过程。

func minWindow(s string, t string) string {
	if t == "" {
		return ""
	}

	//滑动窗口，
	//先移动右指针，遇到让当前窗口满足条件的第一个元素后右指针停下来。
	//然后移动左指针，遇到让当前窗口不满足条件的第一个元素后左指针停下来。

	requiredCharToCharCount := make(map[rune]int)
	for _, rune_ := range t {
		requiredCharToCharCount[rune_] += 1
	}

	holdingCharToCharCount := make(map[rune]int)
	lackingCharSum := 0
	// 窗口[left...right), 和C传统一致，这样可以表示len为0的空串，目标子串可以直接用切片语法[left:right]表示出来
	left, right := 0, 0

	for rune_, count := range requiredCharToCharCount {
		holdingCharToCharCount[rune_] = 0
		lackingCharSum += count
	}

	shortestSubstringRightIdx := 0
	shortestSubstringLen := math.MaxInt32

OuterLoop:
	for {
		for lackingCharSum > 0 {
			if right > len(s)-1 {
				break OuterLoop
			}
			if requiredCount, ok := requiredCharToCharCount[rune(s[right])]; ok {
				holdingCharCount := holdingCharToCharCount[rune(s[right])]
				if holdingCharCount < requiredCount {
					lackingCharSum -= 1
				}
				holdingCharToCharCount[rune(s[right])] += 1
			}
			right += 1
		}

		// 此时已经找到了一个覆盖子串，lackingCharSum == 0

		for lackingCharSum == 0 {

			subStringLen := right - left
			if subStringLen < shortestSubstringLen {
				shortestSubstringLen = subStringLen
				shortestSubstringRightIdx = right
			}

			if requiredCount, ok := requiredCharToCharCount[rune(s[left])]; ok {
				holdingCharToCharCount[rune(s[left])] -= 1
				holdingCharCount := holdingCharToCharCount[rune(s[left])]
				if holdingCharCount < requiredCount {
					lackingCharSum += 1
				}
			}
			left += 1
			// 极端情况下，此时left==right，此时t只有一个字符，总之不会出现left > right的情况
		}

		// 此时左侧擦除了一个元素导致覆盖子串失效, lackingCharSum == 1

	}

	if shortestSubstringRightIdx == 0 {
		return ""
	}
	return s[shortestSubstringRightIdx-shortestSubstringLen : shortestSubstringRightIdx]
}
