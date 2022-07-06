class Solution:
    def integerBreak(self, n: int) -> int:

        # dp[i]表示长度为i的绳子至少割一刀, 所有切割方案中每段绳子长度乘积最大的那个方案取得的乘积
        # 题目所求为dp[n]
        dp: list[int | float] = [-float("inf")] * (n + 1)

        for i in range(n+1):
            if i == 0 or i == 1:
                continue
            elif i == 2:
                dp[i] = 1
            else:
                max_ = -float("inf")
                left_half_len = 1
                while left_half_len < i:
                    right_half_len = i - left_half_len
                    # 左半绳子切0或多刀取得的最大积或因数 * 右半绳子切0或多刀取得的最大积或因数
                    candidate = max(dp[left_half_len], left_half_len) * max(dp[right_half_len], right_half_len)
                    if candidate > max_:
                        max_ = candidate
                    left_half_len += 1
                dp[i] = max_

        return dp[n]
