package data_structure

import (
	"cmp"
	"github.com/davecgh/go-spew/spew"
	"github.com/k0kubun/pp/v3"
	"math/rand"
)

type FHQTreap[K cmp.Ordered, V any] struct {
	Key      K
	Val      V
	L        *FHQTreap[K, V]
	R        *FHQTreap[K, V]
	len      int
	priority float64
}

func (root *FHQTreap[K, V]) searchNodeByKey(key K) *FHQTreap[K, V] {
	if root == nil {
		return nil
	}
	if key == root.Key {
		return root
	} else if key < root.Key {
		return root.L.searchNodeByKey(key)
	} else {
		return root.R.searchNodeByKey(key)
	}
}

func (root *FHQTreap[K, V]) splitByKey(key K) (tree1, freeNode, tree2 *FHQTreap[K, V]) {
	if root == nil {
		return nil, nil, nil
	}
	if key == root.Key {
		tree1, tree2 = root.L, root.R
		root.L, root.R = nil, nil
		root.len = 1
		return tree1, root, tree2
	} else if key < root.Key {
		tree1, freeNode, tree2 = root.L.splitByKey(key)
		root.L = tree2
		root.len = root.L.Len() + 1 + root.R.Len()
		return tree1, freeNode, root
	} else {
		tree1, freeNode, tree2 = root.R.splitByKey(key)
		root.R = tree1
		root.len = root.L.Len() + 1 + root.R.Len()
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
	rootRank := root.L.Len() + 1
	if rank == rootRank {
		tree1, tree2 = root.L, root.R
		root.L, root.R = nil, nil
		root.len = 1
		return tree1, root, tree2
	} else if rank < rootRank {
		tree1, freeNode, tree2 = root.L.splitByRank(rank)
		root.L = tree2
		root.len = root.L.Len() + 1 + root.R.Len()
		return tree1, freeNode, root
	} else {
		tree1, freeNode, tree2 = root.R.splitByRank(rank - rootRank)
		root.R = tree1
		root.len = root.L.Len() + 1 + root.R.Len()
		return root, freeNode, tree2
	}
}

// 调用方要保证root中的key都小于tree中的key
func (root *FHQTreap[K, V]) mergeWith(tree *FHQTreap[K, V]) (newTree *FHQTreap[K, V]) {
	if tree == nil {
		return root
	}
	if root == nil {
		return tree
	}
	if root.priority > tree.priority {
		newTree = root.R.mergeWith(tree)
		root.R = newTree
		root.len = root.L.Len() + 1 + root.R.Len()
		return root
	} else {
		newTree = root.mergeWith(tree.L)
		tree.L = newTree
		tree.len = tree.L.Len() + 1 + tree.R.Len()
		return tree
	}
}

func (root *FHQTreap[K, V]) Len() (len_ int) {
	if root != nil {
		return root.len
	}
	return 0
}

func (root *FHQTreap[K, V]) GetByKey(key K) (val V, rank int, ok bool) {
	node := root.searchNodeByKey(key)
	if node != nil {
		return node.Val, node.L.Len() + 1, true
	}
	return
}

func (root *FHQTreap[K, V]) GetByRank(rank int) (key K, val V) {
	if rank < 0 || rank > root.Len() {
		panic("invalid argument rank")
	}
	rootRank := root.L.Len() + 1
	if rank == rootRank {
		return root.Key, root.Val
	} else if rank < rootRank {
		return root.L.GetByRank(rank)
	} else {
		return root.R.GetByRank(rank - rootRank)
	}
}

func (root *FHQTreap[K, V]) Insert(key K, val V) (newTree *FHQTreap[K, V]) {
	node := root.searchNodeByKey(key)
	if node != nil {
		node.Val = val
		return root
	}
	tree1, freeNode, tree2 := root.splitByKey(key)
	// assert freeNode is nil
	if freeNode != nil {
		panic("unexpected")
	}
	newNode := &FHQTreap[K, V]{
		Key:      key,
		Val:      val,
		L:        nil,
		R:        nil,
		len:      1,
		priority: rand.Float64(),
	}
	return tree1.mergeWith(newNode).mergeWith(tree2)
}

func (root *FHQTreap[K, V]) RemoveByKey(key K) (newTree *FHQTreap[K, V]) {
	node := root.searchNodeByKey(key)
	if node == nil {
		return root
	}
	tree1, freeNode, tree2 := root.splitByKey(key)
	// assert freeNode is not nil
	if freeNode == nil {
		panic("unexpected")
	}
	return tree1.mergeWith(tree2)
}

func (root *FHQTreap[K, V]) RemoveByRank(rank int) (newTree *FHQTreap[K, V]) {
	if rank < 0 || rank > root.Len() {
		panic("invalid argument rank")
	}
	tree1, freeNode, tree2 := root.splitByRank(rank)
	// assert freeNode is not nil
	if freeNode == nil {
		panic("unexpected")
	}
	return tree1.mergeWith(tree2)
}

//算法训练营 陈小玉 5.1 Treap
//https://oi-wiki.org/ds/treap/

//普通有序树中, avl tree、 red black tree 获得一个元素的排名和根据排名获得一个元素的复杂度是n.
//对于本例中的 Treap, 这两个操作复杂度是logn。 Treap 是 augmented search tree 的代表。

func TestFHQTreap() {

	var root *FHQTreap[string, int]

	root = root.Insert("h", 1)
	root = root.Insert("he", 15)
	root = root.Insert("hel", 1500)
	root = root.Insert("hello", 150000)

	pp.Println(root)

	//spew.Dump(root.GetByRank(1))
	//spew.Dump(root.GetByRank(2))
	//spew.Dump(root.GetByRank(3))
	//spew.Dump(root.GetByRank(4))

	root = root.RemoveByKey("h")
	root = root.RemoveByKey("hel")

	spew.Dump(root.GetByKey("h"))
	spew.Dump(root.GetByKey("he"))

	//root = root.RemoveByRank(3)
	//root = root.RemoveByRank(1)
	//
	//spew.Dump(root.GetByRank(1))
	//spew.Dump(root.GetByRank(2))

	//root = root.Insert("helloworld", 100000000)
	//root = root.RemoveByKey("pika")
	//pp.Println(root)
}
