class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        num_sum: int = sum(nums)
        if num_sum % 2 == 1:
            return False
        subset_sum: int = num_sum // 2

        # dp[i][j] 代表num的前i个元素 (也即nums[:i])中能否选出几个元素, 这几个元素的和为j
        # 题目所求结果为 dp[len(nums)][subset_sum] is True
        dp: list[list[bool]] = [[False] * (subset_sum + 1) for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            for j in range(subset_sum + 1):
                if i == 0 or j == 0:
                    if j == 0:
                        dp[i][j] = True
                    else:  # j != 0 and i == 0
                        dp[i][j] = False
                else:
                    dp[i][j] = dp[i-1][j] or (j - nums[i-1] >= 0 and dp[i-1][j - nums[i-1]])

        return dp[len(nums)][subset_sum] is True
