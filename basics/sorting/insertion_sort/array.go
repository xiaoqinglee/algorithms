package insertion_sort

func InsertionSort(array []int) { //使得左边的有序子数组在其内部慢慢膨胀
	for elementToInsert := 1; elementToInsert <= len(array)-1; elementToInsert++ {
		key := array[elementToInsert]
		elementToShift := elementToInsert - 1
		for ; elementToShift >= 0 && array[elementToShift] > key; elementToShift-- {
			array[elementToShift+1] = array[elementToShift]
		}
		//now elementToShift is the index of rightMostElementLessOrEqualThanKey // 插入排序应当是稳定的
		array[elementToShift+1] = key
	}
}
