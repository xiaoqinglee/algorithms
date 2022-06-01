package problems

func LongestSubstringWithoutRepeatingCharacters(s string) int {

	// maxLengthIndexStart := 0
	// maxLengthIndexEnd := 0
	maxLength := 0

	indexStart := 0
	indexEnd := 0
	length := 0
	mapSubstringRuneToIndex := map[rune]int{}

	runes := []rune(s)
	for i, value := range runes {
		if repeatRuneIndex, ok := mapSubstringRuneToIndex[value]; ok {
			for iterIndex := indexStart; iterIndex <= repeatRuneIndex; iterIndex++ {
				delete(mapSubstringRuneToIndex, runes[iterIndex])
			}
			indexStart = repeatRuneIndex + 1
		}
		mapSubstringRuneToIndex[value] = i
		indexEnd = i
		length = indexEnd - indexStart + 1
		if length > maxLength {
			// maxLengthIndexStart = indexStart
			// maxLengthIndexEnd = indexEnd
			maxLength = length
		}
	}
	return maxLength
}
