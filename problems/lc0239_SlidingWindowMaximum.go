package problems

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
	if !(k >= 0 && k <= len(nums)) {
		panic("Invalid Input nums and k")
	}
}
