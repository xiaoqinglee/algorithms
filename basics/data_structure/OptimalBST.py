# 算法导论 第三版 15.5 最优二叉搜索树
# https://www.youtube.com/playlist?list=PL4IH6CVPpTZUwOOyNioJgPnDOnOYO0MO9
# 一棵期望搜索代价最小的二叉搜索树, 我们称之为最优二叉搜索树. 


# root 节点的深度是0
# E[树T的搜索代价]
#     = sum((depth(ki) + 1) * pi for i in [1...n]) + sum((depth(di) + 1) * qi for i in [0...n])
#     = 1 + sum(depth(ki) * pi for i in [1...n]) + sum(depth(di) * qi for i in [0...n])


# [ki...kr-1]构成的二叉搜索树的搜索期望是e[i, r—1]
# [kr+1...j]构成的二叉搜索树的搜索期望是e[r+1, j]
# [i...j]构成的二叉搜索树的搜索期望是e[i, j]
#
# 定义 w(i, j) = sum(pr for r in [i...j]) + sum(qr for r in [i-1...j])
#
# 则有 e[i, j] = pr + (e[i, r—1] + w(i, r—1)) + (e[r+1, j] + w(r+1, j))
#
# 解释:
#     因为左子树高度增加1所以左子树上所有node的高度增加1, 所以向总期望贡献w(i, r—1)
#     因为右子树高度增加1所以右子树上所有node的高度增加1, 所以向总期望贡献w(r+1, j)
#     当前root从无到有, 所以高度也增加1, 向总期望贡献pr
#     所以总的期望增加w(i, j)
#
# 化简得到e[i, j] = e[i, r—1] + e[r+1, j] + w(i, j)


# 选取使得当前二叉树搜索期望最低的方案, 可得最终递归公式：
#
# if j == i - 1:
#     e[i, j] = qi-1
# elif j >= i:
#     e[i, j] = min([(e[i, r—1] + e[r+1, j] + w(i, j)) for r in [i...j]])


# 我们用一个表e[1...n+1, 0...n] 来保存e[i, j]值.
# 第一维下标上界为n+1而不是n, 原因在于对于只包含伪关键字dn的子树, 我们需要计算并保存e[n+1, n].
# 第二维下标下界为0, 是因为对于只包含伪关键字d0的子树, 我们需要计算并保存e[1, O].
# 我们只使用表中满足j>=i的表项e[i, j].
#
# 我们还使用一个表root, 表项root[i, j]记录包含关键字ki, ..., kj的树的根.
# 我们只使用此表中满足1<=i<=j<=n的表项root[i, j].
#
# 我们还需要另一个表来提高计算效率. 为了避免每次计算e[i, j]时都重新计算w(i, j),
# 我们将这些值保存在表w[1...n+1, 0...n]中,
# 对于基本情况:
#     w[i, i-1]=qi-1 for i in [1...n+1]
# 对j>=i 的情况, 可如下计算：
#     w[i, j] = w[i, j-1] + pj + qj

