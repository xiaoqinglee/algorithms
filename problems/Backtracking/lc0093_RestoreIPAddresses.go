package Backtracking

import (
	"strconv"
	"strings"
)

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

	nums_ := make([]string, 4)
	var result []string

	var traverse func([]string, int, int)
	traverse = func(nums []string, hasFixedFirstNNums int, hasConsideredFirstNChars int) {
		if hasFixedFirstNNums == 4 || hasConsideredFirstNChars == len(s) {
			if hasFixedFirstNNums == 4 && hasConsideredFirstNChars == len(s) {
				result = append(result, strings.Join(nums_, "."))
			}
			return
		}

		//rightSideBorder 不包含
		for rightSideBorder := hasConsideredFirstNChars + 1; rightSideBorder <= len(s) && rightSideBorder-hasConsideredFirstNChars <= 3; rightSideBorder += 1 {
			if isValidNum(s[hasConsideredFirstNChars:rightSideBorder]) {
				nums[hasFixedFirstNNums] = s[hasConsideredFirstNChars:rightSideBorder]
				traverse(nums, hasFixedFirstNNums+1, rightSideBorder)
			}
		}
	}
	traverse(nums_, 0, 0)
	return result
}
