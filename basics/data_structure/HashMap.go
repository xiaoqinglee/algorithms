package data_structure

import (
	"container/list"
	"fmt"
	"hash/maphash"
)

//	import "hash/maphash"
//
//	// The zero Hash value is valid and ready to use; setting an
//	// initial seed is not necessary.
//	var h maphash.Hash
//
//	// Add a string to the hash, and print the current hash value.
//	h.WriteString("hello, ")
//	fmt.Printf("%#x\n", h.Sum64())
//
//	// Reset discards all data previously added to the Hash, without
//	// changing its seed.
//	h.Reset()

//	list是个package，内含两个type：
//
//	type Element struct {
//	 next, prev *Element  // 上一个元素和下一个元素
//	 list *List  // 元素所在链表
//	 Value interface{}  // 元素
//	}
//	type List struct {
//	 root Element  // 链表的根元素
//	 len  int      // 链表的长度
//	}
//
//	type Element
//	  func (e *Element) Next() *Element
//	  func (e *Element) Prev() *Element
//	type List
//	  func New() *List
//	  func (l *List) Len() int // 在链表长度
//	  func (l *List) Back() *Element   // 最后一个元素
//	  func (l *List) Front() *Element  // 第一个元素
//	  func (l *List) PushBack(v interface{}) *Element  // 在队列最后插入元素
//	  func (l *List) PushFront(v interface{}) *Element  // 在队列头部插入元素
//	  func (l *List) Remove(e *Element) interface{} // 删除某个元素

type KVPair struct {
	K string
	V interface{}
}

type HashMap struct {
	hashFunc maphash.Hash
	buckets  []*list.List
	len      int

	minNBuckets       int
	growingFactor     int
	loadFactorAverage float32

	loadFactorMin float32
	loadFactorMax float32
}

const (
	GROW   = 1
	SHRINK = -1
)

func NewHashMap() HashMap {
	m := HashMap{
		minNBuckets:       4,
		growingFactor:     4,
		loadFactorAverage: 0.5,
	}
	m.loadFactorMin = m.loadFactorAverage / float32(m.growingFactor)
	m.loadFactorMax = m.loadFactorAverage * float32(m.growingFactor)
	return m
}

func (this *HashMap) rehash(rehashOperation int) {

	// 还未向map中插入值的时候，bucket数目为0; 第一次向map中插入值的时候map值为4, 是bucket数目的非零最小值。
	// bucket数目的取值：0,4,16,32...

	//loadFactor的健康值1/2, 最大极限值2，最小极限值1/8.
	//len增长为原来的4倍 -> bucket数目也增长为原来的4倍，这样loadFactor的值仍为1/2；
	//len缩小为原来的1/4倍 -> bucket数目也缩小为原来的1/4倍，这样loadFactor的值仍为1/2。

	var newNBuckets int
	if rehashOperation == GROW {
		fmt.Println("Growing", len(this.buckets), "->", len(this.buckets)*this.growingFactor)
		newNBuckets = len(this.buckets) * this.growingFactor
	} else if rehashOperation == SHRINK {
		fmt.Println("Shrinking", len(this.buckets), "->", len(this.buckets)/this.growingFactor)
		newNBuckets = len(this.buckets) / this.growingFactor
	}

	oldBuckets := this.buckets
	this.buckets = make([]*list.List, newNBuckets)

	for bucketIndex := range oldBuckets {
		if oldBuckets[bucketIndex] == nil {
			continue
		}
		for node := oldBuckets[bucketIndex].Front(); node != nil; node = node.Next() {
			kVPair := node.Value.(KVPair)
			bucketIdx := this.getBucketIndex(kVPair.K)
			if this.buckets[bucketIdx] == nil {
				this.buckets[bucketIdx] = list.New()
			}
			this.buckets[bucketIdx].PushFront(kVPair)
		}
	}
}

func (this *HashMap) getBucketIndex(key string) int {
	this.hashFunc.WriteString(key)
	this.hashFunc.WriteString("jack&rose") // 防止哈希攻击
	index := int(this.hashFunc.Sum64() % uint64(len(this.buckets)))
	this.hashFunc.Reset()
	return index
}

func (this *HashMap) loadFactor() float32 {
	return float32(this.len) / float32(len(this.buckets))
}

func (this *HashMap) Len() int {
	return this.len
}

func (this *HashMap) Put(key string, value interface{}) {
	if this.len == 0 {
		this.buckets = make([]*list.List, this.minNBuckets)
	}
	bucketIdx := this.getBucketIndex(key)
	if this.buckets[bucketIdx] == nil {
		this.buckets[bucketIdx] = list.New()
	}
	var targetNode *list.Element
	for node := this.buckets[bucketIdx].Front(); node != nil; node = node.Next() {
		if node.Value.(KVPair).K == key {
			targetNode = node
			break
		}
	}
	kVPair := KVPair{
		K: key,
		V: value,
	}
	if targetNode != nil {
		targetNode.Value = kVPair
		return
	}
	this.buckets[bucketIdx].PushFront(kVPair)
	this.len += 1

	if this.loadFactor() > this.loadFactorMax {
		this.rehash(GROW)
	}
}

func (this *HashMap) Get(key string) (val interface{}, ok bool) {
	if this.len == 0 {
		return nil, false
	}
	bucketIdx := this.getBucketIndex(key)
	if this.buckets[bucketIdx] == nil {
		return nil, false
	}
	for node := this.buckets[bucketIdx].Front(); node != nil; node = node.Next() {
		if node.Value.(KVPair).K == key {
			return node.Value.(KVPair).V, true
		}
	}
	return nil, false
}

func (this *HashMap) Remove(key string) (ok bool) {
	if this.len == 0 {
		return false
	}
	bucketIdx := this.getBucketIndex(key)
	if this.buckets[bucketIdx] == nil {
		return false
	}
	var targetNode *list.Element
	for node := this.buckets[bucketIdx].Front(); node != nil; node = node.Next() {
		if node.Value.(KVPair).K == key {
			targetNode = node
			break
		}
	}
	if targetNode == nil {
		return false
	}
	this.buckets[bucketIdx].Remove(targetNode)
	this.len -= 1

	if this.loadFactor() < this.loadFactorMin && len(this.buckets) > this.minNBuckets {
		this.rehash(SHRINK)
	}
	return true
}
