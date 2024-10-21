package DynamicProgramming

// https://leetcode.cn/problems/longest-palindromic-substring/
func longestPalindrome(s string) string {
	if len(s) == 0 {
		return s
	}

	dp := make([][]bool, len(s))
	for i := range dp {
		dp[i] = make([]bool, len(s))
	}
	longestPalindromicSubstringLength := 0
	longestPalindromicSubstring := ""

	populateDpTable := func() {
		for subStringLen := 1; subStringLen <= len(s); subStringLen++ {
			//子串左边界i（包含），右边界j（包含）
			for i := range s {
				j := i + (subStringLen - 1)
				if j >= len(s) {
					break
				}
				if i == j {
					dp[i][j] = true
				} else if i+1 == j {
					dp[i][j] = s[i] == s[j]
				} else {
					dp[i][j] = s[i] == s[j] && dp[i+1][j-1]
				}
				if dp[i][j] && subStringLen > longestPalindromicSubstringLength {
					longestPalindromicSubstring = s[i : j+1]
					longestPalindromicSubstringLength = subStringLen
				}
			}
		}
	}

	populateDpTable()
	return longestPalindromicSubstring
}
