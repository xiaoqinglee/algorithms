package ArrayStackQueue

import "container/list"

//https://leetcode.cn/problems/implement-stack-using-queues

type MyStack struct {
	queue     *list.List
	queueTemp *list.List
}

func Constructor() MyStack {
	return MyStack{queue: list.New(), queueTemp: list.New()}
}

func (myStack *MyStack) Push(x int) {
	myStack.queueTemp.PushBack(x)
	for myStack.queue.Len() > 0 {
		myStack.queueTemp.PushBack(myStack.queue.Remove(myStack.queue.Front()).(int))
	}
	myStack.queue, myStack.queueTemp = myStack.queueTemp, myStack.queue
}

func (myStack *MyStack) Pop() int {
	if myStack.queue.Len() == 0 {
		panic("empty stack")
	}
	return myStack.queue.Remove(myStack.queue.Front()).(int)
}

func (myStack *MyStack) Top() int {
	if myStack.queue.Len() == 0 {
		panic("empty stack")
	}
	return myStack.queue.Front().Value.(int)
}

func (myStack *MyStack) Empty() bool {
	return myStack.queue.Len() == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
