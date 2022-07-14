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
		integer, _ := strconv.Atoi(chars)
		return 0 <= integer && integer <= 255
	}

	nums_ := make([]string, 4)
	var result []string

	var traverse func([]string, int, int)
	traverse = func(nums []string, hasFixedFirstNNums int, hasReadFirstNChars int) {
		if (hasReadFirstNChars == len(s) && hasFixedFirstNNums != 4) ||
			(hasReadFirstNChars != len(s) && hasFixedFirstNNums == 4) {
			return
		}
		if hasReadFirstNChars == len(s) && hasFixedFirstNNums == 4 {
			result = append(result, strings.Join(nums_, "."))
			return
		}

		for rightSideBorder := hasReadFirstNChars + 1; rightSideBorder <= len(s) &&
			rightSideBorder-hasReadFirstNChars <= 3; rightSideBorder += 1 {
			if isValidNum(s[hasReadFirstNChars:rightSideBorder]) {
				nums[hasFixedFirstNNums] = s[hasReadFirstNChars:rightSideBorder]
				traverse(nums, hasFixedFirstNNums+1, rightSideBorder)
			}
		}
	}
	traverse(nums_, 0, 0)
	return result
}
