package TreeTraversal

import (
	"github.com/xiaoqinglee/algorithms/pkg"
	"math"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxPathSum(root *pkg.TreeNode) int {

	// 题目要我们找出经过某一个node和该node的0、1或2个孩子节点形成的路径，
	// 且这个路径上所有节点的权重相加之和最大，求这个权重之和X。

	// 转换问题：
	// 中序遍历可以求得经过任意一个node和该node的0或1个孩子节点形成的路径，
	// 且这个路径上所有节点的权重相加之和最大，和这个和的值Y。

	// 可知
	//X(root) = max(root.Val,
	//              root.Val + Y(root.Left),
	//              root.Val + Y(root.Right),
	//              root.Val + Y(root.Left) + Y(root.Right))

	max := func(int1, int2 int) int {
		if int1 > int2 {
			return int1
		}
		return int2
	}

	result := math.MinInt32

	var singlePathSum func(node *pkg.TreeNode) int
	singlePathSum = func(node *pkg.TreeNode) int {
		if node == nil {
			return 0
		}
		leftPathSum := max(0, singlePathSum(node.Left))
		rightPathSum := max(0, singlePathSum(node.Right))

		resultCandidate := leftPathSum + rightPathSum + node.Val
		result = max(resultCandidate, result)

		return max(leftPathSum, rightPathSum) + node.Val
	}
	singlePathSum(root)
	return result
}
