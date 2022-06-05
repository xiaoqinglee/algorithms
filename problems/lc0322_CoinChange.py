class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        # 和 lc0279 完全平方和数一样，不同的是零钱可能兑换不开。
        coins.sort()

        # 零钱找不开的情景在python这种动态语言中可以使用None，在静态Golang语言中可以使用-1特殊值，使用前判断是否是-1。
        dp: list[int] = [-1] * (amount + 1)
        for i in range(amount + 1):  # 0,1..n
            if i == 0:
                dp[i] = 0
            else:
                # 同样的，静态语言golang中使用特殊值代替None
                min_: int = -1
                for coin in coins:
                    if i - coin < 0:
                        break
                    if dp[i-coin] == -1:
                        continue
                    if min_ == -1:
                        min_ = dp[i-coin]
                    else:
                        min_ = min(dp[i-coin], min_)
                if min_ == -1:
                    dp[i] = -1
                else:
                    dp[i] = min_ + 1

        return dp[amount]
