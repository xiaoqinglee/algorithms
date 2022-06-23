package problems

import (
	"github.com/xiaoqinglee/algorithm/basics/data_structure"
	"strconv"
)

type MyHashMap struct {
	data_structure.HashMap
}

func Constructor() MyHashMap {
	return MyHashMap{data_structure.NewHashMap()}
}

func (this *MyHashMap) Put(key int, value int) {
	this.HashMap.Put(strconv.Itoa(key), value)
}

func (this *MyHashMap) Get(key int) int {
	val, ok := this.HashMap.Get(strconv.Itoa(key))
	if !ok {
		return -1
	}
	return val.(int)
}

func (this *MyHashMap) Remove(key int) {
	this.HashMap.Remove(strconv.Itoa(key))
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
