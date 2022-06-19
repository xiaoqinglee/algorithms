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

	windowCharToCharCount := make(map[rune]int)
	lackingCharSum := 0
	left, right := -1, -1 // 窗口(left...right], right 指针填充一个格子，left 指针擦除一个格子。

	for rune_, count := range requiringCharToCharCount {
		windowCharToCharCount[rune_] = 0
		lackingCharSum += count
	}

	shortestSubstringRightIdx := -1
	shortestSubstringLen := math.MaxInt32
OuterLoop:
	for {
		for lackingCharSum > 0 {
			right += 1
			if right > len(s)-1 {
				break OuterLoop
			}
			if requiringCount, ok := requiringCharToCharCount[rune(s[right])]; ok {
				holdingCharCount := windowCharToCharCount[rune(s[right])]
				if holdingCharCount < requiringCount {
					lackingCharSum -= 1
				}
				windowCharToCharCount[rune(s[right])] += 1
			}
		}

		// 此时已经找到了一个覆盖子串，lackingCharSum == 0

		for lackingCharSum == 0 {

			subStringLen := right - left
			if subStringLen < shortestSubstringLen {
				shortestSubstringLen = subStringLen
				shortestSubstringRightIdx = right
			}

			left += 1
			if requiringCount, ok := requiringCharToCharCount[rune(s[left])]; ok {
				windowCharToCharCount[rune(s[left])] -= 1
				holdingCharCount := windowCharToCharCount[rune(s[left])]
				if holdingCharCount < requiringCount {
					lackingCharSum += 1
				}
			}
		}

		// 此时左侧擦除了一个元素导致覆盖子串失效, lackingCharSum > 0

	}

	if shortestSubstringRightIdx == -1 {
		return ""
	}

	return s[shortestSubstringRightIdx+1-shortestSubstringLen : shortestSubstringRightIdx+1]
}
