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

// https://leetcode.cn/problems/maximum-depth-of-binary-tree
func maxDepth(root *pkg.TreeNode) int {
	if root == nil {
		return 0
	}

	max := func(int1, int2 int) int {
		if int1 > int2 {
			return int1
		}
		return int2
	}

	return max(maxDepth(root.Left), maxDepth(root.Right)) + 1
}
