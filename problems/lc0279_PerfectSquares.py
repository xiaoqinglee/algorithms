class Solution:
    def numSquares(self, n: int) -> int:

        # 相关问题 see lc0322

        if n < 0:
            return 0

        squares: list[int] = []
        for i in range(1, n):
            square = i * i
            if square > n:
                break
            squares.append(square)

        # dp[i]代表和为i的完全平方数的最少数量。
        # dp[i] = min(dp[i - j]) + 1 for j in squares, 要求 i - j >= 0.

        dp: list[int | None] = [None] * (n + 1)
        for i in range(n+1):  # 0,1..n
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = 1
            else:
                min_: int | None = None
                for square in squares:
                    if i - square < 0:
                        break
                    if min_ is None:
                        min_ = dp[i - square]
                    else:
                        min_ = min(dp[i - square], min_)
                dp[i] = min_ + 1
        return dp[n]
