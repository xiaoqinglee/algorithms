pub struct Solution;

use std::collections::HashSet;

// https://leetcode.cn/problems/contains-duplicate
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut set = HashSet::new();
        nums.iter().any(|&x| !set.insert(x))
    }
}
