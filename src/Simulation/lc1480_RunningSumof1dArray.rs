pub struct Solution;

// https://leetcode.cn/problems/running-sum-of-1d-array
impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        nums.iter()
            .scan(0, |state, &x| {
                *state = *state + x;
                Some(*state)
            })
            .collect()
    }
}
