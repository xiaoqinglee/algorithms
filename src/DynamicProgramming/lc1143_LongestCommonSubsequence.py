# https://leetcode.cn/problems/longest-common-subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # text1 长度为 n, text2 长度为 m,
        # 定义数组dp[n][m]
        # dp[i][j] 为 text1 的 [0..i] 子串与 [0..j] 子串(包含右边界)形成的所有公共子序列中长度最长的那个子序列的长度
        # i in [0..n-1]
        # j in [0..m-1]

        dp: list[list[int | None]] = [[None] * len(text2) for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if i == 0 and j == 0:
                    dp[i][j] = 1 if text1[i] == text2[j] else 0
                elif i == 0:
                    dp[i][j] = 1 if any(text1[i] == text2[j_] for j_ in range(0, j + 1)) else 0
                elif j == 0:
                    dp[i][j] = 1 if any(text1[i_] == text2[j] for i_ in range(0, i + 1)) else 0
                else:
                    if text1[i] == text2[j]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1) - 1][len(text2) - 1]
