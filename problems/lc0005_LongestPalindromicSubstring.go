package problems

func LongestPalindromicSubstring(s string) string {

	//不考虑字符串s中包含字节数大于1的rune的情景

	longestLeftCharIndex := 0
	longestRightCharIndex := 0
	longestLength := 0

	leftCharIndex := 0
	rightCharIndex := 0
	length := 0

	charAsCenter := [...]bool{false, true} //false: 以字符的左边界作为中心, true: 以字符本身作为中心
	for i := range s {
		for _, charAsCenter := range charAsCenter {

			if charAsCenter {
				leftCharIndex = i - 1
				rightCharIndex = i + 1
			} else {
				leftCharIndex = i - 1
				rightCharIndex = i
			}

			for {
				if leftCharIndex < 0 || rightCharIndex >= len(s) || s[leftCharIndex] != s[rightCharIndex] {
					break
				}
				leftCharIndex -= 1
				rightCharIndex += 1
			}
			leftCharIndex += 1
			rightCharIndex -= 1

			length = rightCharIndex - leftCharIndex + 1
			if length > longestLength {
				longestLeftCharIndex = leftCharIndex
				longestRightCharIndex = rightCharIndex
				longestLength = length
			}
		}
	}
	return s[longestLeftCharIndex : longestRightCharIndex+1]
}
