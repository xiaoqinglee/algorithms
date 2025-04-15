package bubble_sort

func BubbleSort(array []int) { //使得右边的有序子数组在其左边界慢慢膨胀
	for floatedElementCount := 0; floatedElementCount < len(array)-1; floatedElementCount++ {
		isChanged := false
		for j := 0; j+1 <= len(array)-1-floatedElementCount; j++ {
			if array[j] > array[j+1] { // 冒泡排序应当是稳定的
				array[j], array[j+1] = array[j+1], array[j]
				isChanged = true
			}
		}
		if !isChanged {
			break
		}
	}
}
