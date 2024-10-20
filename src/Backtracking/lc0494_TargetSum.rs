pub struct Solution;

// https://leetcode.cn/problems/target-sum/
// impl Solution {
//
//     // last_used_num_idx + 1 == used_num_count == next_to_use_num_idx
//     pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
//         fn n_ways(nums_ref: &Vec<i32>, target: i32, used_num_count: usize, acc: i32) -> i32 {
//             if used_num_count == nums_ref.len() {
//                 return if acc == target { 1 } else { 0 };
//             }
//             let positive = n_ways(
//                 nums_ref,
//                 target,
//                 used_num_count + 1,
//                 acc + nums_ref[used_num_count],
//             );
//             let negative = n_ways(
//                 nums_ref,
//                 target,
//                 used_num_count + 1,
//                 acc - nums_ref[used_num_count],
//             );
//             positive + negative
//         }
//
//         n_ways(&nums, target, 0, 0)
//     }
// }

// 需要对原问题做一个等价转换:
//
// 等号左边和右边都加上左边所有数字的绝对值之和, 然后左边和右边都除以二.
// 原问题变为: 等号左边的每个数字取 0 个或 1个, 计算和等于等号右边.
// 这样, 原问题就变成了01背包问题.
//
// 对转换后的问题进行建模:
//
// 存在两个变量：
// i 是数组 array 元素的索引，j 是目标和。
// dp[i][j] 表示考虑完左闭右闭区间 array[0..=i]内的所有元素, 构造出和 j 的构造方式数量。
// 最终所求解为 dp[nums.len()-1][target]
impl Solution {
    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
        let temp = target + nums.iter().sum::<i32>();
        let (target, rem) = (temp / 2, temp % 2);
        if target < 0 || rem > 0 {
            return 0;
        }
        let mut matrix = vec![vec![0; (target + 1) as usize]; nums.len()];
        for i in 0..nums.len() {
            for j in 0..=target {
                if i == 0 {
                    matrix[0][j as usize] = (nums[0] * 0 == j) as i32 + (nums[0] * 1 == j) as i32;
                } else {
                    matrix[i][j as usize] = matrix[i - 1][(j - 0) as usize]
                        + if j - nums[i] >= 0 {
                            matrix[i - 1][(j - nums[i]) as usize]
                        } else {
                            0
                        }
                }
            }
        }
        matrix[nums.len() - 1][target as usize]
    }
}
