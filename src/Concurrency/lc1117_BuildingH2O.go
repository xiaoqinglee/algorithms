package Concurrency

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// https://leetcode.cn/problems/building-h2o/

type H2O struct {
	HCount int
	OCount int
	m      sync.Mutex
	HChan  chan struct{}
	OChan  chan struct{}
}

func NewH2O() *H2O {
	return &H2O{
		HCount: 0,
		OCount: 0,
		HChan:  make(chan struct{}, 2),
		OChan:  make(chan struct{}, 1),
	}
}

func (h2o *H2O) Hydrogen() {
	h2o.m.Lock()
	h2o.HCount += 1
	if h2o.HCount >= 2 && h2o.OCount >= 1 {
		h2o.HCount -= 2
		h2o.OCount -= 1
		time.Sleep(2 * time.Second)
		h2o.HChan <- struct{}{}
		h2o.HChan <- struct{}{}
		h2o.OChan <- struct{}{}
	}
	h2o.m.Unlock()
	<-h2o.HChan
	fmt.Print("H")
}

func (h2o *H2O) Oxygen() {
	h2o.m.Lock()
	h2o.OCount += 1
	if h2o.HCount >= 2 && h2o.OCount >= 1 {
		h2o.HCount -= 2
		h2o.OCount -= 1
		time.Sleep(2 * time.Second)
		h2o.HChan <- struct{}{}
		h2o.HChan <- struct{}{}
		h2o.OChan <- struct{}{}
	}
	h2o.m.Unlock()
	<-h2o.OChan
	fmt.Print("O")
}

func TestH2O() {
	var wg sync.WaitGroup
	chars := []string{"H", "H", "O"}
	for i := 0; i < 4; i++ {
		chars = append(chars, chars...)
	}
	rand.Seed(42)
	rand.Shuffle(len(chars), func(i, j int) { chars[i], chars[j] = chars[j], chars[i] })

	h2o := NewH2O()

	wg.Add(len(chars))
	for i := 0; i < len(chars); i++ {
		go func(i int) {
			defer wg.Done()
			if chars[i] == "H" {
				h2o.Hydrogen()
			} else {
				h2o.Oxygen()
			}
		}(i)
	}
	wg.Wait()
}

//https://medium.com/golangspec/reusable-barriers-in-golang-156db1f75d0b
