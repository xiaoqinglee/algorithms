package Concurrency

import (
	"fmt"
	"sync"
)

type ZeroEvenOdd struct {
	n           int
	nextToPrint int  // need protection 保存下一个要打印的非零数字
	zerosTurn   bool // need protection
	cv          *sync.Cond
}

func NewZeroEvenOdd(n int) *ZeroEvenOdd {
	if n <= 0 {
		panic("Invalid Input")
	}
	return &ZeroEvenOdd{
		n:           n,
		nextToPrint: 1,
		zerosTurn:   true,
		cv:          sync.NewCond(&sync.Mutex{}),
	}
}

func (z *ZeroEvenOdd) Zero(printNumberFunc func(a ...any) (n int, err error)) {
	for {
		z.cv.L.Lock()
		for !z.zerosTurn {
			z.cv.Wait()
		}
		printNumberFunc(0)
		if z.nextToPrint == z.n {
			z.zerosTurn = !z.zerosTurn
			z.cv.Broadcast()
			z.cv.L.Unlock()
			fmt.Println("z.nextToPrint is", z.nextToPrint, "Zero is returning")
			return
		} else {
			z.zerosTurn = !z.zerosTurn
			z.cv.Broadcast()
			z.cv.L.Unlock()
		}
	}
}

func (z *ZeroEvenOdd) Odd(printNumberFunc func(a ...any) (n int, err error)) {
	for {
		z.cv.L.Lock()
		for !(!z.zerosTurn && z.nextToPrint%2 == 1) {
			z.cv.Wait()
		}
		printNumberFunc(z.nextToPrint)
		if z.nextToPrint == z.n {
			z.cv.L.Unlock()
			fmt.Println("printed number is", z.nextToPrint, "Odd is returning")
			return
		} else if z.nextToPrint == z.n-1 {
			z.nextToPrint += 1
			z.zerosTurn = !z.zerosTurn
			z.cv.Broadcast()
			z.cv.L.Unlock()
			fmt.Println("printed number is", z.nextToPrint-1, "Odd is returning")
			return
		} else {
			z.nextToPrint += 1
			z.zerosTurn = !z.zerosTurn
			z.cv.Broadcast()
			z.cv.L.Unlock()
		}
	}
}

func (z *ZeroEvenOdd) Even(printNumberFunc func(a ...any) (n int, err error)) {
	for {
		z.cv.L.Lock()
		for !(!z.zerosTurn && z.nextToPrint%2 == 0) {
			z.cv.Wait()
		}
		printNumberFunc(z.nextToPrint)
		if z.nextToPrint == z.n {
			z.cv.L.Unlock()
			fmt.Println("printed number is", z.nextToPrint, "Even is returning")
			return
		} else if z.nextToPrint == z.n-1 {
			z.nextToPrint += 1
			z.zerosTurn = !z.zerosTurn
			z.cv.Broadcast()
			z.cv.L.Unlock()
			fmt.Println("printed number is", z.nextToPrint-1, "Even is returning")
			return
		} else {
			z.nextToPrint += 1
			z.zerosTurn = !z.zerosTurn
			z.cv.Broadcast()
			z.cv.L.Unlock()
		}
	}
}

func TestZeroEvenOdd() {
	zeo := NewZeroEvenOdd(15)
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
