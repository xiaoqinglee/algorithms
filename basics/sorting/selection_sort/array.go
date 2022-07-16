package selection_sort

func SelectionSort(array []int) { //使得左边的有序子数组在其右边界慢慢膨胀
	for selectedElementCount := 0; selectedElementCount < len(array)-1; selectedElementCount++ {
		jMin := selectedElementCount

		for j := selectedElementCount + 1; j <= len(array)-1; j++ {
			if array[j] < array[jMin] {
				jMin = j
			}
		}
		if jMin != selectedElementCount {
			array[selectedElementCount], array[jMin] = array[jMin], array[selectedElementCount]
		}
	}
}
