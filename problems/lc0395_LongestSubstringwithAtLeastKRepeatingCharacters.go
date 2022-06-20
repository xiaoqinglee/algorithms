package problems

import (
	"math"
	"strings"
)

func longestSubstring(s string, k int) int {

	//这个题不能用滑动窗口
	//参考lc0003和lc0076

	//对于字符串 s，如果存在某个字符 ch，它的出现次数大于 0 且小于 k，则任何包含 ch 的子串都不可能满足要求。
	//也就是说，我们将字符串按照 ch 切分成若干段，则满足要求的最长子串一定出现在某个被切分的段内，而不能跨越一个或多个段。
	//因此，可以考虑分治的方式求解本题。

	max := func(int1, int2 int) int {
		if int1 > int2 {
			return int1
		}
		return int2
	}

	if s == "" {
		return 0
	}
	charCount := make(map[rune]int)
	for _, char := range s {
		charCount[char] += 1
	}
	var sep rune
	for char, count := range charCount {
		if count < k {
			sep = char
			break
		}
	}
	if sep == 0 {
		return len(s)
	}
	longestLen := math.MinInt32
	for _, substring := range strings.Split(s, string(sep)) {
		longestLen = max(longestLen, longestSubstring(substring, k))
	}
	return longestLen
}
