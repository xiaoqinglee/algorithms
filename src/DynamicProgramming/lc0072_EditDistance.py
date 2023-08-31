# https://leetcode.cn/problems/edit-distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # min_distance[i][j] 是 word1[:i) 和 word2[:j) 的最小编辑距离
        # 题目所求的是min_distance[len(word1)][len(word2)]
        min_distance: list[list[int | float]] = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    if i == 0:
                        min_distance[i][j] = j
                    else:  # j == 0
                        min_distance[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:  # word1 -> word2: 不操作, 删除, 插入
                        min_distance[i][j] = min(min_distance[i-1][j-1] + 0,
                                                 min_distance[i-1][j] + 1,
                                                 min_distance[i][j-1] + 1)
                    else:  # word1 -> word2: 替换, 删除, 插入
                        min_distance[i][j] = min(min_distance[i-1][j-1] + 1,
                                                 min_distance[i-1][j] + 1,
                                                 min_distance[i][j-1] + 1)

        return min_distance[len(word1)][len(word2)]
