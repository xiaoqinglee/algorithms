pub struct Solution;

use std::collections::HashSet;

// https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
impl Solution {
    // pub fn find_repeat_number(nums: Vec<i32>) -> i32 {
    //     let mut set = HashSet::new();
    //     match nums.iter().find(|&&x| !set.insert(x)) {
    //         Some(&x) => x,
    //         None => panic!("repeated number not found"),
    //     }
    // }
    // pub fn find_repeat_number(nums: Vec<i32>) -> i32 {
    //     let mut num_count = vec![0; nums.len()];
    //     nums.iter().for_each(|&x| num_count[x as usize] += 1);
    //     match num_count.iter().position(|&count| count > 1) {
    //         Some(index) => index as i32,
    //         None => panic!("repeated number not found"),
    //     }
    // }
    pub fn find_repeat_number(nums: Vec<i32>) -> i32 {
        let mut num_count = vec![0; nums.len()];
        match nums.iter().find(|&&num| {
            num_count[num as usize] += 1;
            num_count[num as usize] > 1
        }) {
            Some(&num) => num as i32,
            None => panic!("repeated number not found"),
        }
    }
}
