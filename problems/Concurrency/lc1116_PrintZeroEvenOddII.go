package Concurrency

import (
	"fmt"
	"sync"
)

type ZeroEvenOddII struct {
	n              int
	oddToZeroChan  chan struct{}
	evenToZeroChan chan struct{}
	toOddChan      chan int
	toEvenChan     chan int
}

func NewZeroEvenOddII(n int) *ZeroEvenOddII {
	if n <= 0 {
		panic("Invalid Input")
	}
	return &ZeroEvenOddII{
		n:              n, // n 只读不写
		oddToZeroChan:  make(chan struct{}, 0),
		evenToZeroChan: make(chan struct{}, 0),
		toOddChan:      make(chan int, 0),
		toEvenChan:     make(chan int, 0),
	}
}

func (z *ZeroEvenOddII) Zero(printNumberFunc func(a ...any) (n int, err error)) {
	nextToPrint := 1
	for {
		if nextToPrint > z.n { // Zero 掌控全局
			close(z.toOddChan)
			close(z.toEvenChan)
			return
		}
		printNumberFunc(0)
		if nextToPrint%2 == 1 {
			z.toOddChan <- nextToPrint
			<-z.oddToZeroChan
		} else {
			z.toEvenChan <- nextToPrint
			<-z.evenToZeroChan
		}
		nextToPrint += 1
	}
}

func (z *ZeroEvenOddII) Odd(printNumberFunc func(a ...any) (n int, err error)) {
	for {
		num, ok := <-z.toOddChan
		if !ok {
			close(z.oddToZeroChan)
			return
		}
		printNumberFunc(num)
		z.oddToZeroChan <- struct{}{}
	}
}

func (z *ZeroEvenOddII) Even(printNumberFunc func(a ...any) (n int, err error)) {
	for {
		num, ok := <-z.toEvenChan
		if !ok {
			close(z.evenToZeroChan)
			return
		}
		printNumberFunc(num)
		z.evenToZeroChan <- struct{}{}
	}
}

func TestZeroEvenOddII() {
	zeo := NewZeroEvenOddII(42)
	var wg sync.WaitGroup
	wg.Add(3)
	go func() {
		defer wg.Done()
		zeo.Even(fmt.Println)
	}()
	go func() {
		defer wg.Done()
		zeo.Odd(fmt.Println)
	}()
	go func() {
		defer wg.Done()
		zeo.Zero(fmt.Println)
	}()
	wg.Wait()
}
