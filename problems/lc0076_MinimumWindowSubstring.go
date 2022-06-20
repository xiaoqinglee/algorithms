package problems

import (
	"math"
)

func minWindow(s string, t string) string {

	//滑动窗口，
	//先移动右指针，遇到让当前窗口满足条件的第一个元素后右指针停下来。
	//然后移动左指针，遇到让当前窗口不满足条件的第一个元素后左指针停下来。

	requiringCharToCharCount := make(map[rune]int)
	for _, rune_ := range t {
		requiringCharToCharCount[rune_] += 1
	}

	holdingCharToCharCount := make(map[rune]int)
	lackingCharSum := 0
	// 窗口[left...right), 和C传统一致，这样可以表示len为0的空串，目标子串可以直接用切片语法[left:right]表示出来
	left, right := 0, 0

	for rune_, count := range requiringCharToCharCount {
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
			if requiringCount, ok := requiringCharToCharCount[rune(s[right])]; ok {
				holdingCharCount := holdingCharToCharCount[rune(s[right])]
				if holdingCharCount < requiringCount {
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

			if requiringCount, ok := requiringCharToCharCount[rune(s[left])]; ok {
				holdingCharToCharCount[rune(s[left])] -= 1
				holdingCharCount := holdingCharToCharCount[rune(s[left])]
				if holdingCharCount < requiringCount {
					lackingCharSum += 1
				}
			}
			left += 1
		}

		// 此时左侧擦除了一个元素导致覆盖子串失效, lackingCharSum == 1

	}

	if shortestSubstringRightIdx == 0 {
		return ""
	}
	return s[shortestSubstringRightIdx-shortestSubstringLen : shortestSubstringRightIdx]
}
