package bubble_sort

func BubbleSort(array []int) { //使得右边的有序子数组在其内部慢慢膨胀
	for FloatedElementCount := 0; FloatedElementCount < len(array)-1; FloatedElementCount++ {
		isChanged := false
		for j := 0; j <= len(array)-2-FloatedElementCount; j++ {
			if array[j+1] < array[j] { // 冒泡排序应该是稳定的
				array[j], array[j+1] = array[j+1], array[j]
				isChanged = true
			}
		}
		if !isChanged {
			break
		}
	}
}
