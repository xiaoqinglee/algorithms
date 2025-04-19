package Simulation

import "strings"

// https://leetcode.cn/problems/zigzag-conversion
func convert(s string, numRows int) string {
	if numRows == 0 {
		panic("Invalid input numRows")
	}
	if numRows <= 1 || len([]rune(s)) < numRows {
		return s
	}
	rows := make([][]string, numRows)
	for i := range rows {
		rows[i] = make([]string, 0)
	}
	var input []string
	for _, char := range s {
		input = append(input, string(char))
	}
	oneIterationProcessNElems := (numRows - 1) * 2
	for range oneIterationProcessNElems - (len(input) % oneIterationProcessNElems) {
		input = append(input, "")
	}
	curCharIdx := 0
	for {
		for i := 0; i <= numRows-2; i++ {
			rows[i] = append(rows[i], input[curCharIdx])
			curCharIdx++
		}
		for i := numRows - 1; i >= 1; i-- {
			rows[i] = append(rows[i], input[curCharIdx])
			curCharIdx++
		}
		if curCharIdx == len(input) {
			break
		}
	}
	var result []string
	for _, row := range rows {
		for _, char := range row {
			result = append(result, char)
		}
	}
	return strings.Join(result, "")
}
