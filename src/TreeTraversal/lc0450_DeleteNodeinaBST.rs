// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use crate::util::data_structure::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

pub struct Solution;

// https://leetcode.cn/problems/delete-node-in-a-bst
impl Solution {
    pub fn delete_node(
        root: Option<Rc<RefCell<TreeNode>>>,
        key: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        fn _pre_node(tree: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
            // 要求 tree 非空, 且 tree 一定存在 pre node
            let mut node = tree.as_ref().unwrap().borrow().left.clone();
            while node.is_some() && node.as_ref().unwrap().borrow().right.is_some() {
                let temp = node.as_ref().unwrap().borrow().right.clone();
                node = temp
            }
            node
        }

        fn _remove(tree: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
            // 要求 tree 非空
            if tree.as_ref().unwrap().borrow().left.is_none() {
                return tree.as_ref().unwrap().borrow().right.clone();
            }
            if tree.as_ref().unwrap().borrow().right.is_none() {
                return tree.as_ref().unwrap().borrow().left.clone();
            }
            let pre = _pre_node(tree.clone());
            assert!(pre.is_some());
            pre.as_ref().unwrap().borrow_mut().right =
                tree.as_ref().unwrap().borrow().right.clone();
            tree.as_ref().unwrap().borrow().left.clone()
        }

        fn _dfs(root: Option<Rc<RefCell<TreeNode>>>, key: i32) -> Option<Rc<RefCell<TreeNode>>> {
            if root.is_none() {
                return None;
            }
            if key == root.as_ref().unwrap().borrow().val {
                _remove(root.clone())
            } else if key < root.as_ref().unwrap().borrow().val {
                let temp = _dfs(root.as_ref().unwrap().borrow().left.clone(), key);
                root.as_ref().unwrap().borrow_mut().left = temp;
                root
            } else {
                let temp = _dfs(root.as_ref().unwrap().borrow().right.clone(), key);
                root.as_ref().unwrap().borrow_mut().right = temp;
                root
            }
        }

        _dfs(root, key)
    }
}
