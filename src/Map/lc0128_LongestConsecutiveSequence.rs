use std::collections::HashSet;

pub struct Solution;

// https://leetcode.cn/problems/longest-consecutive-sequence/
impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let num_set: HashSet<_> = nums.into_iter().collect();
        let mut ans = 0;
        for &num in &num_set {
            if !num_set.contains(&(num - 1)) {
                let count = (num..).take_while(|x| num_set.contains(x)).count();
                ans = ans.max(count);
            }
        }
        ans as i32
    }
}
