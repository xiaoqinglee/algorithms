package Concurrency

import (
	"fmt"
	"sync"
)

type ZeroEvenOdd struct {
	n       int
	current int
	turn    int // 0 1 2 3 轮转. 0 2 zero活动. 1, 3 其他两个函数活动.
	cv      *sync.Cond
}

func NewZeroEvenOdd(n int) *ZeroEvenOdd {
	if n <= 0 {
		panic("Invalid Input")
	}
	return &ZeroEvenOdd{
		n:       n,
		current: 1,
		turn:    0,
		cv:      sync.NewCond(&sync.Mutex{}),
	}
}

func (z *ZeroEvenOdd) Zero(printNumberFunc func(a ...any) (n int, err error)) {
	for {
		z.cv.L.Lock()
		for z.turn != 0 && z.turn != 2 {
			z.cv.Wait()
		}
		if z.current <= z.n {
			printNumberFunc(0)
		}
		z.turn = (z.turn + 1) % 4
		z.cv.Broadcast()
		z.cv.L.Unlock()
		if z.current > z.n && z.turn == 3 {
			return
		}
	}
}

func (z *ZeroEvenOdd) Odd(printNumberFunc func(a ...any) (n int, err error)) {
	for {
		z.cv.L.Lock()
		for z.turn != 1 {
			z.cv.Wait()
		}
		if z.current <= z.n {
			printNumberFunc(z.current)
		}
		z.current += 1
		z.turn = (z.turn + 1) % 4
		z.cv.Broadcast()
		z.cv.L.Unlock()
		if z.current > z.n {
			return
		}
	}
}

func (z *ZeroEvenOdd) Even(printNumberFunc func(a ...any) (n int, err error)) {
	for {
		z.cv.L.Lock()
		for z.turn != 3 {
			z.cv.Wait()
		}
		if z.current <= z.n {
			printNumberFunc(z.current)
		}
		z.current += 1
		z.turn = (z.turn + 1) % 4
		z.cv.Broadcast()
		z.cv.L.Unlock()
		if z.current > z.n {
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
