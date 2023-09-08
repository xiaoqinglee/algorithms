pub struct Solution;

//https://leetcode.cn/problems/rotate-image/
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        // 做两次变换: 第一次沿着右上左下对角线对折, 第二次沿着左中间右中间直线对折
        dbg!(&matrix);
        let n = matrix.len();
        for i in 0..n {
            for j in 0..n {
                if i + j >= n {
                    continue;
                }
                (matrix[i][j], matrix[n - 1 - j][n - 1 - i]) =
                    (matrix[n - 1 - j][n - 1 - i], matrix[i][j])
            }
        }
        for i in 0..n {
            for j in 0..n {
                if i >= n / 2 {
                    continue;
                }
                (matrix[i][j], matrix[n - 1 - i][j]) = (matrix[n - 1 - i][j], matrix[i][j])
            }
        }
        dbg!(&matrix);
    }
}
