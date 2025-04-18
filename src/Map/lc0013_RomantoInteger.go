package Map

// https://leetcode.cn/problems/roman-to-integer
func romanToInt(s string) int {
	symbolToValue := map[string]int{
		"I":  1,
		"V":  5,
		"X":  10,
		"IV": 4,
		"IX": 9,
		"L":  50,
		"C":  100,
		"XL": 40,
		"XC": 90,
		"D":  500,
		"M":  1000,
		"CD": 400,
		"CM": 900,
	}

	result := 0

	for currentIdx := 0; currentIdx <= len(s)-1; {

		canMakeTwoSteps := false
		if currentIdx+1 <= len(s)-1 {
			if _, ok := symbolToValue[s[currentIdx:currentIdx+2]]; ok {
				canMakeTwoSteps = true
			}
		}

		if canMakeTwoSteps {
			result += symbolToValue[s[currentIdx:currentIdx+2]]
			currentIdx += 2
		} else {
			result += symbolToValue[s[currentIdx:currentIdx+1]]
			currentIdx += 1
		}
	}

	return result
}
