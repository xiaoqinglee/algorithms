package insertion_sort

func InsertionSort(array []int) { //使得左边的有序子数组在其内部慢慢膨胀
	for elementToInsert := 1; elementToInsert <= len(array)-1; elementToInsert++ {
		var elementToShift int
		for elementToShift = elementToInsert - 1; elementToShift >= 0 && array[elementToShift] > array[elementToInsert]; elementToShift-- { // 插入排序应当是稳定的
			array[elementToShift+1] = array[elementToShift]
		}
		//now elementToShift is the index of theRightMostElementLessOrEqualThanTheKey
		array[elementToShift+1] = array[elementToInsert]
	}
}
