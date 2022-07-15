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

		//rightSideBorder 不包含
		for rightSideBorder := hasSolvedFirstNChars + 1; rightSideBorder <= len(s) && rightSideBorder-hasSolvedFirstNChars <= 3; rightSideBorder += 1 {
			if isValidNum(s[hasSolvedFirstNChars:rightSideBorder]) {
				nums_ = append(nums_, s[hasSolvedFirstNChars:rightSideBorder])
				traverse(rightSideBorder)
				nums_ = nums_[:len(nums_)-1]
			}
		}
	}
	traverse(0)
	return result
}
