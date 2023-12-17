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

// https://leetcode.cn/problems/successor-lcci
func inorderSuccessor(root *TreeNode, p *TreeNode) *TreeNode {
	// 二叉树节点的前继后继节点就是这个二叉树中序遍历结果顺序中前一个元素和后一个元素
	// 利用BST区别于普通二叉树的性质可以加快搜索

	var findSuccessor func(node *TreeNode) *TreeNode
	findSuccessor = func(node *TreeNode) *TreeNode {
		if node == nil {
			return nil
		}
		if node.Val <= p.Val {
			return findSuccessor(node.Right)
		} else {
			successor := findSuccessor(node.Left)
			if successor == nil {
				return node
			} else {
				return successor
			}
		}
	}
	return findSuccessor(root)
}
