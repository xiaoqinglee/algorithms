package TreeTraversal

//// This is the interface that allows for creating nested lists.
//// You should not implement it, or speculate about its implementation
//type NestedInteger struct {
//}
//
//// Return true if this NestedInteger holds a single integer, rather than a nested list.
//func (this NestedInteger) IsInteger() bool {}
//
//// Return the single integer that this NestedInteger holds, if it holds a single integer
//// The result is undefined if this NestedInteger holds a nested list
//// So before calling this method, you should have a check
//func (this NestedInteger) GetInteger() int {}
//
//// Set this NestedInteger to hold a single integer.
//func (n *NestedInteger) SetInteger(value int) {}
//
//// Set this NestedInteger to hold a nested list and adds a nested integer to it.
//func (this *NestedInteger) Add(elem NestedInteger) {}
//
//// Return the nested list that this NestedInteger holds, if it holds a nested list
//// The list length is zero if this NestedInteger holds a single integer
//// You can access NestedInteger's List element directly if you want to modify it
//func (this NestedInteger) GetList() []*NestedInteger {}

const (
	LIST     = 0
	INTVALUE = 1
)

type NodeType int

type Node struct {
	nodeType             NodeType
	list                 []*NestedInteger
	listNextReadingIndex int
	intValue             int
}

type NestedIterator struct {
	nodeStack            []*Node
	currNode             *Node
	nextValue            int
	nextValuePreComputed bool
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
	iter := &NestedIterator{currNode: &Node{
		nodeType:             LIST,
		list:                 nestedList,
		listNextReadingIndex: 0,
	}}
	return iter
}

func (this *NestedIterator) produceOneChild(listTypeNodeInTree *Node) (aChildToInsert *Node) {
	if listTypeNodeInTree.listNextReadingIndex > len(listTypeNodeInTree.list)-1 {
		return nil
	}
	nestedInteger := listTypeNodeInTree.list[listTypeNodeInTree.listNextReadingIndex]
	listTypeNodeInTree.listNextReadingIndex += 1
	var newNode *Node
	if nestedInteger.IsInteger() {
		newNode = &Node{
			nodeType: INTVALUE,
			intValue: nestedInteger.GetInteger(),
		}
	} else {
		newNode = &Node{
			nodeType:             LIST,
			list:                 nestedInteger.GetList(),
			listNextReadingIndex: 0,
		}
	}
	return newNode
}

func (this *NestedIterator) next() (element int, ok bool) {

	currNode := this.currNode

	for currNode != nil || len(this.nodeStack) > 0 {

		for currNode != nil {

			this.nodeStack = append(this.nodeStack, currNode)

			if currNode.nodeType == LIST {
				currNode = this.produceOneChild(currNode)
			} else if currNode.nodeType == INTVALUE {
				ok = true
				element = currNode.intValue
				currNode = nil
			}
		}

		this.nodeStack = this.nodeStack[:len(this.nodeStack)-1]
		if len(this.nodeStack) > 0 {
			topNode := this.nodeStack[len(this.nodeStack)-1]
			currNode = this.produceOneChild(topNode)
		}

		if ok {
			this.currNode = currNode
			break
		}
	}
	return element, ok
}

func (this *NestedIterator) Next() int {
	if this.nextValuePreComputed {
		this.nextValuePreComputed = false
		return this.nextValue
	} else {
		element, ok := this.next()
		if ok {
			return element
		} else {
			panic("No more value")
		}
	}
}

func (this *NestedIterator) HasNext() bool {
	if this.nextValuePreComputed {
		return true
	} else {
		element, ok := this.next()
		if ok {
			this.nextValue = element
			this.nextValuePreComputed = true
			return true
		} else {
			return false
		}
	}
}
