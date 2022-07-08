package Concurrency

import (
	"fmt"
	"sync"
)

type Foo struct {
	name         string
	firstIsDone  chan struct{}
	secondIsDone chan struct{}
}

func NewFoo(name string) *Foo {
	return &Foo{
		name:         name,
		firstIsDone:  make(chan struct{}, 0),
		secondIsDone: make(chan struct{}, 0),
	}
}

func (foo *Foo) First() {
	fmt.Println("In instance: ", foo.name, "First")
	close(foo.firstIsDone)
}

func (foo *Foo) Second() {
	<-foo.firstIsDone
	fmt.Println("In instance: ", foo.name, "Second")
	close(foo.secondIsDone)
}

func (foo *Foo) Third() {
	<-foo.secondIsDone
	fmt.Println("In instance: ", foo.name, "Third")
}

func TestFoo() {

	//三个不同的线程 A、B、C 将会共用一个 Foo 实例。
	//
	//    线程 A 将会调用 first() 方法
	//    线程 B 将会调用 second() 方法
	//    线程 C 将会调用 third() 方法
	//
	//请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。

	var wg sync.WaitGroup
	wg.Add(6)
	instance1 := NewFoo("1")
	go func() {
		defer wg.Done()
		instance1.First()
	}()
	go func() {
		defer wg.Done()
		instance1.Second()
	}()
	go func() {
		defer wg.Done()
		instance1.Third()
	}()

	instance2 := NewFoo("2")
	go func() {
		defer wg.Done()
		instance2.Third()
	}()
	go func() {
		defer wg.Done()
		instance2.Second()
	}()
	go func() {
		defer wg.Done()
		instance2.First()
	}()

	fmt.Println("All sub work is inited.")
	wg.Wait()
	fmt.Println("All sub work is finished.")
}

//cap 大于 1 的 chan 实现信号量
//cap 为 1 的 chan 实现 01 信号量, 也即互斥锁
//cap 为 0 的 chan 实现 condition variable.
