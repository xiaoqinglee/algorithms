# https://leetcode.cn/problems/house-robber
class Solution:
    def rob(self, nums: list[int]) -> int:

        # dp[i] 代表考虑完下标为i的那一家受害者之后盗贼能够拥有的最大赃物总价值信息
        # dp[i][1] 代表考虑完下标为i的那一家受害者并抢了他之后盗贼能够拥有的最大赃物总价值
        # dp[i][0] 代表考虑完下标为i的那一家受害者并放过他之后盗贼能够拥有的最大赃物总价值
        dp: list[list[int | None]] = [[None, None] for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = nums[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + 0
                dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[len(nums)-1][0], dp[len(nums)-1][1])
