pub struct Solution;

use std::collections::HashSet;

impl Solution {
    // pub fn find_repeat_number(nums: Vec<i32>) -> i32 {
    //     let mut set = HashSet::new();
    //     match nums.iter().find(|&&x| set.insert(x) == false) {
    //         Some(&x) => x,
    //         _ => panic!("repeated number not found"),
    //     }
    // }
    pub fn find_repeat_number(nums: Vec<i32>) -> i32 {
        let mut num_count = vec![0; nums.len()];
        nums.iter().for_each(|&x| num_count[x as usize] += 1);
        match num_count.iter().position(|&count| count > 1) {
            Some(index) => index as i32,
            _ => panic!("repeated number not found"),
        }
    }
}
