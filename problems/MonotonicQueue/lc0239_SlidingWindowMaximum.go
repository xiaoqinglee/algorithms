package MonotonicQueue

import (
	"container/list"
	"fmt"
)

//	list是个package，内含两个type：
//
//	type Element struct {
//	 next, prev *Element  // 上一个元素和下一个元素
//	 list *List  // 元素所在链表
//	 Value interface{}  // 元素
//	}
//	type List struct {
//	 root Element  // 链表的根元素
//	 len  int      // 链表的长度
//	}
//
//	type Element
//	  func (e *Element) Next() *Element
//	  func (e *Element) Prev() *Element
//	type List
//	  func New() *List
//	  func (l *List) Len() int // 在链表长度
//	  func (l *List) Back() *Element   // 最后一个元素
//	  func (l *List) Front() *Element  // 第一个元素
//	  func (l *List) PushBack(v interface{}) *Element  // 在队列最后插入元素
//	  func (l *List) PushFront(v interface{}) *Element  // 在队列头部插入元素
//	  func (l *List) Remove(e *Element) interface{} // 删除某个元素

//List可以当做双端队列使用
func TestList() {
	fmt.Println("===========================")
	queue := list.New()
	queue.PushBack(1)
	queue.PushBack(2)
	queue.PushFront(0)
	fmt.Println(queue.Len())
	fmt.Println(queue.Front().Value)
	fmt.Println(queue.Back().Value)
	fmt.Println("===========================")
	queueBackInFrontOut := list.New()
	queueBackInFrontOut.PushBack(42)
	fmt.Println(queueBackInFrontOut.Front().Value)
	queueBackInFrontOut.Remove(queueBackInFrontOut.Front())
	fmt.Println("===========================")
	queueFrontInBackOut := list.New()
	queueFrontInBackOut.PushFront(42)
	fmt.Println(queueFrontInBackOut.Back().Value)
	queueFrontInBackOut.Remove(queueFrontInBackOut.Back())
	fmt.Println("===========================")
}

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
