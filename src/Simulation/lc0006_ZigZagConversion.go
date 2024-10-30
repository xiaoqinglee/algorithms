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

	rows := make([][]rune, numRows)
	for i := range rows {
		rows[i] = make([]rune, 0)
	}
	var movingDirectionUpToDown []bool
	for i := 0; i < numRows-1; i++ {
		movingDirectionUpToDown = append(movingDirectionUpToDown, true)
	}
	for i := 0; i < numRows-1; i++ {
		movingDirectionUpToDown = append(movingDirectionUpToDown, false)
	}

	movingDirectionIndex := -1
	currentRow := 0
	rows[currentRow] = append(rows[currentRow], []rune(s)[0])

	for _, rune_ := range []rune(s[1:]) {
		movingDirectionIndex = (movingDirectionIndex + 1 + len(movingDirectionUpToDown)) % len(movingDirectionUpToDown)
		upToDown := movingDirectionUpToDown[movingDirectionIndex]
		if upToDown {
			currentRow += 1
		} else {
			currentRow -= 1
		}
		rows[currentRow] = append(rows[currentRow], rune_)
	}
	strings_ := make([]string, numRows)
	for _, row := range rows {
		strings_ = append(strings_, string(row))
	}
	result := strings.Join(strings_, "")
	return result
}
