package SlidingWindow

// https://leetcode.cn/problems/sliding-window-maximum
func maxSlidingWindow(nums []int, k int) []int {

	//使用双端队列维护当前窗口内的元素值。
	//新进入窗口的元素在队尾入队，挤出窗口的元素在队头出队。新进入窗口的元素在队尾入队时会有部分元素在队尾出队。
	//保持整个队列队尾元素小于等于队头元素，满足单调栈，这样队头总是窗口内最大元素。

	if !(k >= 0 && k <= len(nums)) {
		panic("Invalid Input nums and k")
	}

	type ValAndIndex struct {
		Val   int
		Index int
	}

	var result []int
	var queue []*ValAndIndex

	for i, num := range nums[:k] {
		for len(queue) > 0 && num > queue[len(queue)-1].Val {
			queue = queue[:len(queue)-1]
		}
		queue = append(queue, &ValAndIndex{num, i})
	}
	result = append(result, queue[0].Val)

	//窗口[left..right]左右边界都包含
	for right := k; right <= len(nums)-1; right++ {
		left := right - (k - 1)
		if queue[0].Index == left-1 {
			queue = queue[1:]
		}
		for len(queue) > 0 && nums[right] > queue[len(queue)-1].Val {
			queue = queue[:len(queue)-1]
		}
		queue = append(queue, &ValAndIndex{nums[right], right})
		//fmt.Printf("enqueue %d %q \n", nums[right], queue)
		result = append(result, queue[0].Val)
	}
	return result
}
