class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # dp[i][...] 为第i（0 <= i <= len(prices - 1)）天闭市时手中持股与否对应的最大资产。
        # dp[i][0] 代表天闭市时手中不持股（又分为当天没动和当天售出两个情况）：
        #       dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] 代表天闭市时手中持股（又分为当天没动和当买入出两个情况）：
        #       dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])

        if len(prices) == 0:
            return 0

        dp: list[list[int]] = [[0, 0]] * len(prices)

        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])

        return dp[len(prices) - 1][0]
