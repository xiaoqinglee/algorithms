package data_structure

import (
	"github.com/davecgh/go-spew/spew"
	"math/rand"
)

type key interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64 | ~string
}

type FHQTreap[K key, V any] struct {
	len      int
	key      K
	val      V
	priority float64
	l        *FHQTreap[K, V]
	r        *FHQTreap[K, V]
}

func (root *FHQTreap[K, V]) splitByKey(key K) (tree1, freeNode, tree2 *FHQTreap[K, V]) {
	if root == nil {
		return nil, nil, nil
	}
	if key == root.key {
		tree1, tree2 = root.l, root.r
		root.l, root.r = nil, nil
		return tree1, root, tree2
	} else if key < root.key {
		tree1, freeNode, tree2 = root.l.splitByKey(key)
		root.l = tree2
		root.len -= tree1.Len()
		root.len -= freeNode.Len()
		return tree1, freeNode, root
	} else {
		tree1, freeNode, tree2 = root.r.splitByKey(key)
		root.r = tree1
		root.len -= tree2.Len()
		root.len -= freeNode.Len()
		return root, freeNode, tree2
	}
}

func (root *FHQTreap[K, V]) splitByRank(rank int) (tree1, freeNode, tree2 *FHQTreap[K, V]) {
	if rank < 0 || rank > root.Len() {
		panic("invalid argument rank")
	}
	if root == nil {
		return nil, nil, nil
	}
	rootRank := root.l.Len() + 1
	if rank == rootRank {
		tree1, tree2 = root.l, root.r
		root.l, root.r = nil, nil
		root.len = 1
		return tree1, root, tree2
	} else if rank < rootRank {
		tree1, freeNode, tree2 = root.l.splitByRank(rank)
		root.l = tree2
		root.len -= tree1.Len()
		root.len -= 1
		return tree1, freeNode, root
	} else {
		tree1, freeNode, tree2 = root.r.splitByRank(rank - rootRank)
		root.r = tree1
		root.len -= tree2.Len()
		root.len -= 1
		return root, freeNode, tree2
	}
}

func (root *FHQTreap[K, V]) mergeWith(tree *FHQTreap[K, V]) (newTree *FHQTreap[K, V]) {
	// 要求root中的key都小于tree中的key, 而且不会overlap
	if tree == nil {
		return root
	}
	if root == nil {
		return tree
	}
	if root.priority > tree.priority {
		newTree = root.r.mergeWith(tree)
		root.r = newTree
		root.len += tree.len
		return root
	} else {
		newTree = root.mergeWith(tree.l)
		tree.l = newTree
		tree.len += root.len
		return tree
	}
}

func (root *FHQTreap[K, V]) search(key K) *FHQTreap[K, V] {
	if root == nil {
		return nil
	}
	if key == root.key {
		return root
	} else if key < root.key {
		return root.l.search(key)
	} else {
		return root.r.search(key)
	}
}

func (root *FHQTreap[K, V]) Get(key K) (val V, ok bool) {
	node := root.search(key)
	if node != nil {
		return node.val, true
	}
	return
}

func (root *FHQTreap[K, V]) GetByRank(rank int) (key K, val V) {
	if rank < 0 || rank > root.Len() {
		panic("invalid argument rank")
	}
	rootRank := root.l.Len() + 1
	if rank == rootRank {
		return root.key, root.val
	} else if rank < rootRank {
		return root.l.GetByRank(rank)
	} else {
		return root.r.GetByRank(rank - rootRank)
	}
}

func (root *FHQTreap[K, V]) Insert(key K, val V) (newTree *FHQTreap[K, V]) {
	node := root.search(key)
	if node != nil {
		node.val = val
		return root
	}
	tree1, _, tree2 := root.splitByKey(key)
	// assert freeNode is nil
	newNode := &FHQTreap[K, V]{
		len:      1,
		key:      key,
		val:      val,
		priority: rand.Float64(),
		l:        nil,
		r:        nil,
	}
	return tree1.mergeWith(newNode).mergeWith(tree2)
}

func (root *FHQTreap[K, V]) Remove(key K) (newTree *FHQTreap[K, V]) {
	node := root.search(key)
	if node == nil {
		return root
	}
	tree1, _, tree2 := root.splitByKey(key)
	// assert freeNode is not nil
	return tree1.mergeWith(tree2)
}

func (root *FHQTreap[K, V]) RemoveByRank(rank int) (newTree *FHQTreap[K, V]) {
	if rank < 0 || rank > root.Len() {
		panic("invalid argument rank")
	}
	tree1, _, tree2 := root.splitByRank(rank)
	// assert freeNode is not nil
	return tree1.mergeWith(tree2)
}

func (root *FHQTreap[K, V]) Len() (len_ int) {
	len_ = 0
	if root != nil {
		len_ += root.len
	}
	return len_
}

func TestFHQTreap() {

	var root *FHQTreap[string, int]

	root = root.Insert("h", 1)
	root = root.Insert("he", 15)
	root = root.Insert("hel", 1500)
	root = root.Insert("hello", 150000)

	//spew.Dump(root)

	//spew.Dump(root.GetByRank(1))
	//spew.Dump(root.GetByRank(2))
	//spew.Dump(root.GetByRank(3))
	//spew.Dump(root.GetByRank(4))

	//root = root.Remove("he")
	//root = root.Remove("h")

	//spew.Dump(root.GetByRank(1))
	//spew.Dump(root.GetByRank(2))

	//root = root.RemoveByRank(2)
	//root = root.RemoveByRank(1)

	//spew.Dump(root.GetByRank(1))
	//spew.Dump(root.GetByRank(2))

	spew.Dump(root.Get("h"))
	spew.Dump(root.Get("he"))

}
