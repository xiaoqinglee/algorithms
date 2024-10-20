package Backtracking

import (
	"strconv"
	"strings"
)

// https://leetcode.cn/problems/restore-ip-addresses/
func restoreIpAddresses(s string) []string {
	isValidNum := func(chars string) bool {
		if len(chars) > 1 && chars[0] == '0' {
			return false
		}
		if len(chars) <= 2 {
			return true
		}
		integer, _ := strconv.Atoi(chars)
		return 0 <= integer && integer <= 255
	}

	var nums_ []string
	var result []string

	var traverse func(int)
	traverse = func(hasSolvedFirstNChars int) {
		if len(nums_) == 4 || hasSolvedFirstNChars == len(s) {
			if len(nums_) == 4 && hasSolvedFirstNChars == len(s) {
				result = append(result, strings.Join(nums_, "."))
			}
			return
		}

		//子串包含rightSideBorder上的字符
		for rightSideBorder := hasSolvedFirstNChars; rightSideBorder <= len(s)-1 && rightSideBorder-hasSolvedFirstNChars+1 <= 3; rightSideBorder += 1 {
			if isValidNum(s[hasSolvedFirstNChars : rightSideBorder+1]) {
				nums_ = append(nums_, s[hasSolvedFirstNChars:rightSideBorder+1])
				traverse(rightSideBorder + 1)
				nums_ = nums_[:len(nums_)-1]
			}
		}
	}
	traverse(0)
	return result
}
