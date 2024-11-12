package TreeTraversal

import . "github.com/xiaoqinglee/algorithms/pkg"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {

	//递归，后序遍历，回退的的时候如果发现当前树第一次集齐了 p q 两个node，那么这个树的根就是 p q 最低的公共祖先target。
	//注意：当找到target之后就不要继续深入向下遍历其他子树了，直接一步一步回退到根节点，将调用栈弹空即可。

	var traverse func(node *TreeNode) (containingPQCount int, target *TreeNode)
	traverse = func(node *TreeNode) (containingPQCount int, target *TreeNode) {
		if node == nil {
			return 0, nil
		}
		leftChildContainingPQCount, target := traverse(node.Left)
		if target != nil {
			return leftChildContainingPQCount, target
		}
		rightChildContainingPQCount, target := traverse(node.Right)
		if target != nil {
			return rightChildContainingPQCount, target
		}
		rootContainingPQCount := 0
		if node == p || node == q {
			rootContainingPQCount = 1
		}
		treeContainingPQCount := rootContainingPQCount + leftChildContainingPQCount + rightChildContainingPQCount

		if treeContainingPQCount == 2 {
			return treeContainingPQCount, node
		}
		return treeContainingPQCount, nil
	}
	_, target := traverse(root)
	return target
}
