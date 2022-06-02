package problems

func LongestSubstringWithoutRepeatingCharacters(s string) int {
	indexStart := 0 //包含
	indexEnd := 0   //包含
	length := 0
	maxLength := length
	substringRuneToIndexMap := map[rune]int{}
	runes := []rune(s)
	for i, rune_ := range runes {
		if repeatingRuneIndex, ok := substringRuneToIndexMap[rune_]; ok {
			for iterIndex := indexStart; iterIndex <= repeatingRuneIndex; iterIndex++ {
				// The built in delete function removes an entry from the map:
				//delete(m, "route")
				//The delete function doesn’t return anything, and will do nothing if the specified key doesn’t exist.
				//但是此处不会出现key不存在的情况，因为子串中没有重复rune，所以不会出现同一个rune key删两遍的情景。
				delete(substringRuneToIndexMap, runes[iterIndex])
			}
			indexStart = repeatingRuneIndex + 1
		}
		substringRuneToIndexMap[rune_] = i
		indexEnd = i
		length = indexEnd - indexStart + 1
		if length > maxLength {
			maxLength = length
		}
	}
	return maxLength
}
