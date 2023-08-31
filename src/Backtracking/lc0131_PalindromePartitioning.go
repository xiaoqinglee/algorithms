package Backtracking

// https://leetcode.cn/problems/palindrome-partitioning/
func partition(s string) [][]string {

	//isPalindrome[i][j]为true, 代表字符串左闭右闭区间[i...j]是回文串
	var isPalindrome [][]bool
	isPalindrome = make([][]bool, len(s), len(s))
	for i := 0; i < len(s); i += 1 {
		isPalindrome[i] = make([]bool, len(s), len(s))
	}

	populateIsPalindrome := func() {
		for palindromeLen := 1; palindromeLen <= len(s); palindromeLen += 1 {
			for palindromeFirstIdx := 0; palindromeFirstIdx+palindromeLen-1 <= len(s)-1; palindromeFirstIdx += 1 {
				//判断s[palindromeFirstIdx...palindromeFirstIdx+palindromeLen-1]是否是回文串
				is := false
				if palindromeLen == 1 {
					is = true
				} else if palindromeLen == 2 {
					is = s[palindromeFirstIdx] == s[palindromeFirstIdx+palindromeLen-1]
				} else {
					is = s[palindromeFirstIdx] == s[palindromeFirstIdx+palindromeLen-1] &&
						isPalindrome[palindromeFirstIdx+1][palindromeFirstIdx+palindromeLen-1-1]
				}
				isPalindrome[palindromeFirstIdx][palindromeFirstIdx+palindromeLen-1] = is
			}
		}
	}
	populateIsPalindrome()

	var partitions [][]string
	var currenPartition []string

	var backtrace func(int)
	backtrace = func(hasSolvedFirstNChars int) {
		if hasSolvedFirstNChars == len(s) {
			currenPartitionCopy := make([]string, len(currenPartition), len(currenPartition))
			copy(currenPartitionCopy, currenPartition)
			partitions = append(partitions, currenPartitionCopy)
			return
		}

		for subStringLastCharIndex := hasSolvedFirstNChars; subStringLastCharIndex <= len(s)-1; subStringLastCharIndex += 1 {
			if isPalindrome[hasSolvedFirstNChars][subStringLastCharIndex] {
				currenPartition = append(currenPartition, s[hasSolvedFirstNChars:subStringLastCharIndex+1])
				backtrace(subStringLastCharIndex + 1)
				currenPartition = currenPartition[:len(currenPartition)-1]
			}
		}
	}

	backtrace(0)

	return partitions
}
