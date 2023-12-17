# https://leetcode.cn/problems/coin-change
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


# 背包问题分类方法:
#     按模型: 01背包、 完全背包
#     按模型中的约束条件: weight "小于等于"、 "等于"
#     按所求目标: 是否存在可行方案、可行方案数量、可行方案列表、可行方案中某一属性的极值、某一属性达到该极值的方案详情。
# 
# 
# 
# 例1.
#     有N种物品和一个容量是W的背包。每种物品有且只有一件。
#     第i种物品的体积是weight[i]，价值是value[i]。
#     将哪些物品装入背包，可使这些物品的总体积小于等于背包容量，且总价值最大，求这个最大的总价值。
#     (等价表述: 填充背包使填充物的总体积小于等于背包容量，存在多种可行方案，
#             这些方案中填充物总价值最大是多少，总价值最大的方案详情也许不唯一)
# 
#     问题分类: 01, 小于等于, 求可行方案中某一属性的极值
# 
# 例2.
#     有N种物品和一个容量是W的背包。每种物品有无数件。
#     第i种物品的体积是weight[i]，价值是value[i]。
#     求解将哪些物品装入背包，可使这些物品的总体积小于等于背包容量，且总价值最大。
#     [等价表述: 同上]
# 
#     问题分类: 完全, 小于等于, 求可行方案中某一属性的极值
# 
# 
#
# 具体例题:
# 
# 
#     322. 零钱兑换
#     https://leetcode.cn/problems/coin-change/
#     分类: 完全, 等于, 求可行方案中某一属性的极值: 方案中物品件数的最小值
# 
# 
#         建模方法1.
#         定义 f[i][j] 为考虑完前 i (i in [1...N]) 种物品，恰好存放于容量等于 j (j in [0...W]) 的背包，
#         所有可行方案中物品件数的最小值[0...Inf]，如果不存在可行方案那么f[i][j] == None
#
#         for j in [0...W]:
#             f[1][j] = (j // weight[1]) if j % weight[1] == 0 else None
#
#         # 递归过程考虑一种多件物品
#         f[i][j] = min(f[i−1][j] + 0, min( (f[i−1][j−k∗weight[i]] + k) for k in [1...Inf] if j−k∗weight[i] >= 0))
#         #要求参与运算的f[i−1][...]都不为None
#
#         建模方法2.
#         定义 f[j] 为考虑所有种类物品，恰好存放于容量等于 j (j in [0...W]) 的背包，
#         所有可行方案中物品件数的最小值[0...Inf]，如果不存在可行方案那么f[j] == None
#
#         f[0] = 0
#
#         # 递归过程仅仅考虑一件物品
#         f[j] = min( (f[j−weight[i]] + 1) for i in [1...N] if j−weight[i] >= 0)  #要求参与运算的f[...]都不为None
#
#
#     518. 零钱兑换 II
#     https://leetcode.cn/problems/coin-change-ii/
#     分类: 完全, 等于, 求可行方案数量
# 
#
#         定义 f[i][j] 为考虑完前 i (i in [1...N]) 种物品，恰好存放于容量等于 j (j in [0...W]) 的背包，的所有可行方案总数[0...Inf]
#         如果不存在可行方案那么f[i][j] == 0
#
#         for j in [0...W]:
#             f[1][j] = 1 if j % weight[1] == 0 else 0
#
#         f[i][j] = sum(f[i−1][j] * 1, sum( (f[i−1][j−k∗weight[i]] * 1) for k in [1...Inf] if j−k∗weight[i] >= 0 ))
#
#
#         另一个建模方法在该求解目标上使用是错误的: （原因: 子问题被重复累加， 考虑问题7元钱，被[3,4]找零的方案总数）
#         定义 f[j] 为考虑所有种类物品，恰好存放于容量等于 j (i in [0...W]) 的背包，所有可行方案总数[0...Inf]
#         如果不存在可行方案那么f[j] == 0
#
#         f[0] = 1
#
#         # 递归过程仅仅考虑一件物品
#         f[j] = sum( (f[j−weight[i]] * 1) for i in [1...N] if j−weight[i] >= 0)
#
#
#
# 其他例题:
#
#
#     416. 分割等和子集
#     https://leetcode.cn/problems/partition-equal-subset-sum/
#     分类: 01, 等于, 求是否存在可行方案
#
#
#     494. 目标和
#     https://leetcode.cn/problems/target-sum/
#     分类: 1/-1背包问题, 等于, 求可行方案数量
#
#
#     39. 组合总和
#     https://leetcode.cn/problems/combination-sum/
#     分类: 完全, 等于, 求可行方案列表
#
#
#     回溯方法可以解决所有待求目标:
#         可行方案列表 （只有回溯方法可以解决，动态规划没法解决）
#         是否存在可行方案: 可行方案列表不为空
#         可行方案数量: 可行方案列表长度
#         可行方案中某一属性的极值: 遍历可行方案列表
#         某一属性达到该极值的方案详情: 遍历可行方案列表
#
