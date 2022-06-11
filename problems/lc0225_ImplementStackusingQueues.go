package problems

import "container/list"

type MyStack struct {
	stack *list.List
	temp  *list.List
}

func Constructor() MyStack {
	return MyStack{stack: list.New(), temp: list.New()}
}

func (this *MyStack) Push(x int) {
	this.temp.PushBack(x)
	for this.stack.Len() > 0 {
		this.temp.PushBack(this.stack.Front().Value.(int))
		this.stack.Remove(this.stack.Front())
	}
	this.stack, this.temp = this.temp, this.stack
}

func (this *MyStack) Pop() int {
	if this.Empty() {
		panic("Empty stack")
	}
	val := this.stack.Front().Value.(int)
	this.stack.Remove(this.stack.Front())
	return val
}

func (this *MyStack) Top() int {
	if this.Empty() {
		panic("Empty stack")
	}
	val := this.stack.Front().Value.(int)
	return val
}

func (this *MyStack) Empty() bool {
	return this.stack.Len() == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
