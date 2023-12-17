package BinarySearch

// https://leetcode.cn/problems/search-a-2d-matrix-ii
func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}

	//如下图所示 中间的元素15将矩阵分成四个左上、右下、左下和右上四个矩形，
	//左上右下有一个公共元素15，左下右上没有公共元素。
	//左上所有元素中除了15外都小于15，右下所有元素中除了15外都大于15。
	//左下既有小于15的元素也有大于15的元素（当然可能有等于15的元素）。
	//右上既有小于15的元素也有大于15的元素（当然可能有等于15的元素）。

	//[
	//	+----------------+---------+
	//	| [1,   4,    7, | 11, 15],|
	//	| [2,   5,    8, | 12, 19],|
	//			   +-----+---------+
	//	| [3,   6, | 15, | 16, 22],|
	//	+----------+-----+         |
	//	| [10, 13, | 16,   17, 24],|
	//	| [18, 21, | 23,   26, 30] |
	//	+----------+---------------+
	//]

	//从右上角开始出发，向左下角趋步。
	//如果当前元素大于目标元素，左移一格；如果当前元素小于目标元素，下移一格。

	row, col := 0, len(matrix[0])-1
	for row <= len(matrix)-1 && col >= 0 {
		if matrix[row][col] < target {
			row += 1
		} else if matrix[row][col] > target {
			col -= 1
		} else { //matrix[row][col] == target
			return true
		}
	}
	return false
}
