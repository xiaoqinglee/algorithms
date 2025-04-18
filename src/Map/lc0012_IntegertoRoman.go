package Map

import (
	"maps"
	"slices"
	"strings"
)

// https://leetcode.cn/problems/integer-to-roman/
func intToRoman(num int) string {
	valueToSymbol := map[int]string{
		1:    "I",
		5:    "V",
		10:   "X",
		4:    "IV",
		9:    "IX",
		50:   "L",
		100:  "C",
		40:   "XL",
		90:   "XC",
		500:  "D",
		1000: "M",
		400:  "CD",
		900:  "CM",
	}

	values := slices.Collect(maps.Keys(valueToSymbol))
	slices.Sort(values)
	slices.Reverse(values)

	var result []string
	for _, value := range values {
		count := num / value
		num = num % value
		for i := 0; i < count; i++ {
			result = append(result, valueToSymbol[value])
		}
	}

	return strings.Join(result, "")
}
