package Concurrency

import (
	"fmt"
	"sync"
)

type ZeroEvenOdd struct {
	n           int
	nextToPrint int  // need protection
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
		if z.nextToPrint <= z.n {
			printNumberFunc(0)
		}
		nextToPrintCopy := z.nextToPrint
		z.zerosTurn = !z.zerosTurn
		z.cv.Broadcast()
		z.cv.L.Unlock()
		if nextToPrintCopy > z.n {
			fmt.Println("next to print:", nextToPrintCopy, "Zero return")
			return
		}
	}
}

func (z *ZeroEvenOdd) Odd(printNumberFunc func(a ...any) (n int, err error)) {
	for {
		z.cv.L.Lock()
		for !(!z.zerosTurn && z.nextToPrint%2 == 1) {
			z.cv.Wait()
		}
		if z.nextToPrint <= z.n {
			printNumberFunc(z.nextToPrint)
		}
		z.nextToPrint += 1
		nextToPrintCopy := z.nextToPrint
		z.zerosTurn = !z.zerosTurn
		z.cv.Broadcast()
		z.cv.L.Unlock()
		if nextToPrintCopy > z.n {
			fmt.Println("next to print:", nextToPrintCopy, "Odd return")
			return
		}
	}
}

func (z *ZeroEvenOdd) Even(printNumberFunc func(a ...any) (n int, err error)) {
	for {
		z.cv.L.Lock()
		for !(!z.zerosTurn && z.nextToPrint%2 == 0) {
			z.cv.Wait()
		}
		if z.nextToPrint <= z.n {
			printNumberFunc(z.nextToPrint)
		}
		z.nextToPrint += 1
		nextToPrintCopy := z.nextToPrint
		z.zerosTurn = !z.zerosTurn
		z.cv.Broadcast()
		z.cv.L.Unlock()
		if nextToPrintCopy > z.n {
			fmt.Println("next to print:", nextToPrintCopy, "Even return")
			return
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
