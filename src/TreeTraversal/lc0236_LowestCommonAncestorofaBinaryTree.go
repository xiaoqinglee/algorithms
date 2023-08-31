package TreeTraversal

import "github.com/xiaoqinglee/algorithms/pkg"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree
func lowestCommonAncestor(root, p, q *pkg.TreeNode) *pkg.TreeNode {

	//递归，后序遍历，回退的的时候如果发现当前树第一次集齐了 p q 两个node，那么这个树的根就是 p q 最低的公共祖先target。
	//注意：当找到target之后就不要继续深入向下遍历其他子树了，直接一步一步回退到根节点，将调用栈弹空即可。

	var target *pkg.TreeNode

	var containingPQCount func(node *pkg.TreeNode) int
	// 如果返回值为-1说明target已经找到了
	containingPQCount = func(node *pkg.TreeNode) int {
		if node == nil {
			return 0
		}
		leftChildContainingPQCount := containingPQCount(node.Left)
		if leftChildContainingPQCount == -1 {
			return -1
		}
		rightChildContainingPQCount := containingPQCount(node.Right)
		if rightChildContainingPQCount == -1 {
			return -1
		}
		rootContainingPQCount := 0
		if node == p || node == q {
			rootContainingPQCount = 1
		}
		treeContainingPQCount := rootContainingPQCount + leftChildContainingPQCount + rightChildContainingPQCount

		if treeContainingPQCount == 2 {
			target = node
			return -1
		}
		return treeContainingPQCount
	}
	containingPQCount(root)
	return target
}
