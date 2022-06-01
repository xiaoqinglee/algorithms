package problems

func ZigZagConversion(s string, numRows int) string {
	runes := []rune(s)
	if len(runes) < numRows {
		numRows = len(runes)
	}
	if numRows == 1 {
		return s
	}
	rows := make([][]rune, numRows)
	topToDown := true
	rowNo := 0
	for _, rune_ := range runes {
		rows[rowNo] = append(rows[rowNo], rune_)
		if topToDown {
			if rowNo < len(rows)-1 {
				rowNo += 1
			} else {
				topToDown = !topToDown
				rowNo -= 1
			}
		} else {
			if rowNo > 0 {
				rowNo -= 1
			} else {
				topToDown = !topToDown
				rowNo += 1
			}
		}
	}
	result := ""
	for _, value := range rows {
		result += string(value)
	}
	return result
}
