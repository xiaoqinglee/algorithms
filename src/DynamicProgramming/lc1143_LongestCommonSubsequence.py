# https://leetcode.cn/problems/longest-common-subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # text1 长度为 n, text2 长度为 m,
        # 定义数组dp[n+1][m+1]
        # dp[i][j] 为 text1 的 [0..i-1] 子串与 [0..j-1] 子串(包含右边界)形成的所有公共子序列中长度最长的那个子序列的长度

        dp: list[list[int | None]] = [[None] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # def _longest_common_subsequence(i, j) -> int:
        #     if dp[i][j] is not None:
        #         return dp[i][j]
        #
        #     if i == 0 or j == 0:
        #         result = 0
        #     else:
        #         if text1[i - 1] == text2[j - 1]:
        #             result = _longest_common_subsequence(i - 1, j - 1) + 1
        #         else:
        #             result = max(_longest_common_subsequence(i - 1, j), _longest_common_subsequence(i, j - 1))
        #
        #     dp[i][j] = result
        #     return result
        #
        # return _longest_common_subsequence(len(text1), len(text2))

        for i in range(len(text1) + 1):
            for j in range(len(text2) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if text1[i - 1] == text2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]
