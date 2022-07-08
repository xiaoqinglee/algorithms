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

func (foo *Foo) First(printFirst func()) {
	fmt.Println("In instance: ", foo.name)
	printFirst()
	close(foo.firstIsDone)
}

func (foo *Foo) Second(printSecond func()) {
	<-foo.firstIsDone
	fmt.Println("In instance: ", foo.name)
	printSecond()
	close(foo.secondIsDone)
}

func (foo *Foo) Third(printThird func()) {
	<-foo.secondIsDone
	fmt.Println("In instance: ", foo.name)
	printThird()
}

func PrinterProvider(toPrint string) func() {
	return func() {
		fmt.Println(toPrint)
	}
}

func TestFoo() {
	printerFuncs := [3]func(){
		PrinterProvider("Fir"),
		PrinterProvider("Sec"),
		PrinterProvider("Thi"),
	}
	var wg sync.WaitGroup
	instance1 := NewFoo("1")
	wg.Add(1)
	go func() {
		defer wg.Done()
		instance1.First(printerFuncs[0])
	}()
	wg.Add(1)
	go func() {
		defer wg.Done()
		instance1.Second(printerFuncs[1])
	}()
	wg.Add(1)
	go func() {
		defer wg.Done()
		instance1.Third(printerFuncs[2])
	}()

	instance2 := NewFoo("2")
	wg.Add(1)
	go func() {
		defer wg.Done()
		instance2.First(printerFuncs[0])
	}()
	wg.Add(1)
	go func() {
		defer wg.Done()
		instance2.Third(printerFuncs[2])
	}()
	wg.Add(1)
	go func() {
		defer wg.Done()
		instance2.Second(printerFuncs[1])
	}()

	instance3 := NewFoo("3")
	wg.Add(1)
	go func() {
		defer wg.Done()
		instance3.Third(printerFuncs[2])
	}()
	wg.Add(1)
	go func() {
		defer wg.Done()
		instance3.Second(printerFuncs[1])
	}()
	wg.Add(1)
	go func() {
		defer wg.Done()
		instance3.First(printerFuncs[0])
	}()

	fmt.Println("Sub work is inited.")
	wg.Wait()
	fmt.Println("All sub work is finished.")
}

//cap 大于 1 的 chan 实现信号量
//cap 为 1 的 chan 实现 01 信号量, 也即互斥锁
//cap 为 0 的 chan 实现 condition variable.
