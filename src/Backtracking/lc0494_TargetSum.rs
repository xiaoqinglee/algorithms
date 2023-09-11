pub struct Solution;

// https://leetcode.cn/problems/target-sum/
impl Solution {
    // pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
    //     fn n_ways(nums_ref: &Vec<i32>, target: i32, last_used_num_idx: i32, acc: i32) -> i32 {
    //         if last_used_num_idx == nums_ref.len() as i32 - 1 {
    //             return if acc == target { 1 } else { 0 };
    //         }
    //         let positive = n_ways(
    //             nums_ref,
    //             target,
    //             last_used_num_idx + 1,
    //             acc + nums_ref[(last_used_num_idx + 1) as usize],
    //         );
    //         let negative = n_ways(
    //             nums_ref,
    //             target,
    //             last_used_num_idx + 1,
    //             acc - nums_ref[(last_used_num_idx + 1) as usize],
    //         );
    //         positive + negative
    //     }
    //
    //     n_ways(&nums, target, -1, 0)
    // }

    // last_used_num_idx + 1 == used_num_count == next_to_use_num_idx
    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
        fn n_ways(nums_ref: &Vec<i32>, target: i32, used_num_count: usize, acc: i32) -> i32 {
            if used_num_count == nums_ref.len() {
                return if acc == target { 1 } else { 0 };
            }
            let positive = n_ways(
                nums_ref,
                target,
                used_num_count + 1,
                acc + nums_ref[used_num_count],
            );
            let negative = n_ways(
                nums_ref,
                target,
                used_num_count + 1,
                acc - nums_ref[used_num_count],
            );
            positive + negative
        }

        n_ways(&nums, target, 0, 0)
    }
}
