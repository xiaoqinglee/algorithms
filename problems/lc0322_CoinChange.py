class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        # 相关问题 see lc0279, 和完全平方和数一样，不同的是零钱可能兑换不开。

        coins.sort()

        # 零钱找不开的情景在python这种动态语言中可以使用None，在静态Golang语言中可以使用-1特殊值，使用前判断是否是-1。
        # dp[i] 代表将总额为i的大钱用coins中的小钱兑换开，coins中每种面额有无限张，所有兑换方案中总张数最少的那个兑换方案中的张数。
        dp: list[int] = [-1] * (amount + 1)
        for amount_ in range(amount + 1):  # 0,1..n
            if amount_ == 0:
                dp[amount_] = 0
            else:
                # 同样的，静态语言golang中使用特殊值代替None
                n_coins_min: int = -1
                for coin in coins:
                    if amount_ - coin < 0:
                        break
                    if dp[amount_-coin] == -1:
                        continue
                    if n_coins_min == -1:
                        n_coins_min = dp[amount_-coin] + 1
                    else:
                        n_coins_min = min(dp[amount_-coin] + 1, n_coins_min)
                if n_coins_min == -1:
                    dp[amount_] = -1
                else:
                    dp[amount_] = n_coins_min

        return dp[amount]
