package SlidingWindow

// https://leetcode.cn/problems/sliding-window-maximum
func maxSlidingWindow(nums []int, k int) []int {

	//使用双端队列维护当前窗口内的元素值
	//首先，如果队头元素正是被移除出窗口的元素，那么将队头元素dequeue，否则什么都不做。
	//其次，当进入窗口的新元素等于或小于队尾元素时enqueue，大于队尾元素时持续在队尾将队尾元素dequeue，直到新元素等于或小于队尾元素并enqueue新元素。

	//保持整个队列队尾元素小于等于队头元素，这样队头最大的元素dequeue后，第二大的元素成为了新的队头。

	if !(k >= 0 && k <= len(nums)) {
		panic("Invalid Input nums and k")
	}

	var result []int
	var queue []int

	//窗口[left..right]
	for right := range nums {
		left := right - k + 1
		if left-1 >= 0 && nums[left-1] == queue[0] {
			queue = queue[1:]
		}
		for len(queue) > 0 && queue[len(queue)-1] < nums[right] {
			queue = queue[:len(queue)-1]
		}
		queue = append(queue, nums[right])
		if left >= 0 {
			result = append(result, queue[0])
		}
	}
	return result
}
