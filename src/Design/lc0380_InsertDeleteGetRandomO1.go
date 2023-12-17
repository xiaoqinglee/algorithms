package Design

import (
	"math/rand"
	"time"
)

// https://leetcode.cn/problems/insert-delete-getrandom-o1/

type RandomizedSet struct {
	keys          []int
	keyToKeyIndex map[int]int
	rand_         *rand.Rand
}

func Constructor() RandomizedSet {
	s := rand.NewSource(time.Now().UnixNano())
	r := rand.New(s)
	return RandomizedSet{keyToKeyIndex: make(map[int]int), rand_: r}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.keyToKeyIndex[val]; ok {
		return false
	}

	this.keys = append(this.keys, val)
	this.keyToKeyIndex[val] = len(this.keys) - 1

	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	if index, ok := this.keyToKeyIndex[val]; ok {
		if index != len(this.keys)-1 {
			this.keys[index] = this.keys[len(this.keys)-1]
			this.keyToKeyIndex[this.keys[index]] = index
		}
		this.keys = this.keys[:len(this.keys)-1]
		delete(this.keyToKeyIndex, val)
		return true
	}
	return false
}

func (this *RandomizedSet) GetRandom() int { //无副作用的
	randomIndex := this.rand_.Intn(len(this.keys))
	return this.keys[randomIndex]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
