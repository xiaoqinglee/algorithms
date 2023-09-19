// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
use crate::util::data_structure::ListNode;

pub struct Solution;

// https://leetcode.cn/problems/reverse-linked-list
impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() {
            return None;
        }
        let mut head = head;
        let mut new_list_head: Option<Box<ListNode>> = None;

        while let Some(mut free_node) = head {
            // let new_head= free_node.next;
            //
            // // //error[E0382]: use of moved value: `free_node.next`
            // // dbg!(free_node.next);
            // free_node.next = new_list_head;

            let new_head = free_node.next.take();

            assert_eq!(free_node.next, None);
            free_node.next = new_list_head;
            new_list_head = Some(free_node);

            head = new_head;
        }
        new_list_head
    }
}
