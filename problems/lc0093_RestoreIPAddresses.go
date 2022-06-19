package problems

import (
	"strconv"
	"strings"
)

func restoreIpAddresses(s string) []string {
	isValidNum := func(chars string) bool {
		if len(chars) == 1 {
			return true
		}
		if len(chars) > 1 && chars[0] == '0' {
			return false
		}
		integer, _ := strconv.Atoi(chars)
		return 0 <= integer && integer <= 255
	}

	nums_ := make([]string, 4)
	var result []string

	var traverse func(nums []string, fixedFirstNNums int, readFirstNChars int)
	traverse = func(nums []string, fixedFirstNNums int, readFirstNChars int) {
		if (readFirstNChars == len(s) && fixedFirstNNums != 4) ||
			(readFirstNChars != len(s) && fixedFirstNNums == 4) {
			return
		}
		if readFirstNChars == len(s) && fixedFirstNNums == 4 {
			result = append(result, strings.Join(nums_, "."))
			return
		}

		for rightSideBorder := readFirstNChars + 1; rightSideBorder <= len(s) &&
			rightSideBorder-readFirstNChars <= 3; rightSideBorder += 1 {
			if isValidNum(s[readFirstNChars:rightSideBorder]) {
				nums[fixedFirstNNums] = s[readFirstNChars:rightSideBorder]
				traverse(nums, fixedFirstNNums+1, rightSideBorder)
			}
		}
	}
	traverse(nums_, 0, 0)
	return result
}
