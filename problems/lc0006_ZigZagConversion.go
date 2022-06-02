package problems

import "strings"

func ZigZagConversion(s string, numRows int) string {
	if numRows == 0 {
		panic("Invalid input numRows")
	}
	if len(s) < numRows {
		numRows = len(s)
	}
	if numRows <= 1 {
		return s
	}

	rows := make([][]rune, numRows)
	for i := range rows {
		rows[i] = make([]rune, 0)
	}
	currentDirectionIsFromTopToDown := true
	currentRow := 0

	shouldTurnAround := func() bool {
		return currentDirectionIsFromTopToDown && currentRow == numRows-1 ||
			!currentDirectionIsFromTopToDown && currentRow == 0
	}

	for _, rune_ := range []rune(s) {
		rows[currentRow] = append(rows[currentRow], rune_)
		if shouldTurnAround() {
			currentDirectionIsFromTopToDown = !currentDirectionIsFromTopToDown
		}
		if currentDirectionIsFromTopToDown {
			currentRow += 1
		} else {
			currentRow -= 1
		}
	}
	strings_ := make([]string, numRows)
	for _, rows := range rows {
		strings_ = append(strings_, string(rows))
	}
	result := strings.Join(strings_, "")
	return result
}
