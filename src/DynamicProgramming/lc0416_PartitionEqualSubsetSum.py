# https://leetcode.cn/problems/partition-equal-subset-sum
class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        num_sum: int = sum(nums)
        if num_sum % 2 == 1:
            return False
        subset_sum: int = num_sum // 2

        # dp[i][j] 代表考虑完num的index i元素，也即nums[:i+1]中能否选出几个元素, 这几个元素的和为j
        # 题目所求结果为 dp[len(nums)-1][subset_sum] is True
        dp: list[list[bool]] = [[False] * (subset_sum + 1) for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(subset_sum + 1):
                if j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = nums[i] == j
                else:
                    dp[i][j] = dp[i - 1][j] or (j - nums[i] >= 0 and dp[i - 1][j - nums[i]])

        return dp[len(nums) - 1][subset_sum] is True
