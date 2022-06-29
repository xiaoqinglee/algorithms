from pkg.data_structure import TreeNode


class OptimalBST:
    def __init__(self, *, p: list[float], q: list[float]):
        assert len(p) > 0 and len(p) + 1 == len(q)
        n = len(p)
        p.insert(0, None)  # 使得 p q 坐标对齐

        # 读写权利只属于对应的记忆化函数, 其他人不可以直接访问
        e_matrix: list[list[float | None]] = [[None] * (n + 1) for _ in range(n + 2)]

        def e_func(i: int, j: int) -> float:
            if e_matrix[i][j] is not None:
                return e_matrix[i][j]

            if j == i - 1:
                result = q[i - 1]
            elif j >= i:
                e_min = float("inf")
                for r in range(i, j + 1):
                    e_candidate = e_func(i, r - 1) + e_func(r + 1, j) + w_func(i, j)
                    if e_candidate < e_min:
                        root = r
                        e_min = e_candidate
                root_matrix[i][j] = root
                result = e_min
            else:
                raise "invalid argument i: {} j:{}".format(i, j)

            e_matrix[i][j] = result
            return result

        w_matrix: list[list[float | None]] = [[None] * (n + 1) for _ in range(n + 2)]

        def w_func(i: int, j: int) -> float:
            if w_matrix[i][j] is not None:
                return w_matrix[i][j]

            if j == i - 1:
                result = q[i - 1]
            elif j >= i:
                result = w_func(i, j - 1) + p[j] + q[j]
            else:
                raise "invalid argument i: {} j:{}".format(i, j)

            w_matrix[i][j] = result
            return result

        root_matrix: list[list[int | None]] = [[None] * (n + 1) for _ in range(n + 2)]

        def root_func(i: int, j: int) -> int:
            return root_matrix[i][j]

        def build_tree(i: int, j: int) -> TreeNode | None:
            if i > j:
                return None
            if i == j:
                return TreeNode(val=i)
            r = root_func(i, j)
            left = build_tree(i, r - 1)
            right = build_tree(r + 1, j)
            return TreeNode(val=r, left=left, right=right)

        e_func(1, n)
        self.root: TreeNode = build_tree(1, n)


def test_optimal_bst():
    tree = OptimalBST(p=[0.15, 0.10, 0.05, 0.10, 0.20], q=[0.05, 0.10, 0.05, 0.05, 0.05, 0.10])


# 算法导论 第三版 15.5 最优二叉搜索树
# 一棵期望搜索代价最小的二叉搜索树, 我们称之为最优二叉搜索树.
# https://www.youtube.com/playlist?list=PL4IH6CVPpTZUwOOyNioJgPnDOnOYO0MO9


# Formally, given a
# sequence K = 〈k1, k2, …, kn〉 of n distinct keys such that k1 < k2 < … <
# kn, build a binary search tree containing them. For each key ki, you are
# given the probability pi that any given search is for key ki. Since some
# searches may be for values not in K, you also have n + 1 “dummy” keys
# d0, d1, d2, …, dn representing those values. In particular, d0 represents
# all values less than k1, dn represents all values greater than kn, and for i
# = 1, 2, …, n − 1, the dummy key di represents all values between ki and
# ki+1. For each dummy key di, you have the probability qi that a search
# corresponds to di. Each key ki is an internal node, and each dummy key di is a
# leaf. Every search is either successful (finding some key ki) or
# unsuccessful (finding some dummy key di).


# root 节点的深度是0
# E[树T的搜索代价]
#     = sum((depth(ki) + 1) * pi for i in [1...n]) + sum((depth(di) + 1) * qi for i in [0...n])
#     = 1 + sum(depth(ki) * pi for i in [1...n]) + sum(depth(di) * qi for i in [0...n])


# [ki...kr-1]构成的二叉搜索树的搜索期望是e[i, r-1]
# [kr+1...j]构成的二叉搜索树的搜索期望是e[r+1, j]
# [i...j]构成的二叉搜索树的搜索期望是e[i, j]
#
# 定义 w(i, j) = sum(pr for r in [i...j]) + sum(qr for r in [i-1...j])
#
# 则有 e[i, j] = pr + (e[i, r-1] + w(i, r-1)) + (e[r+1, j] + w(r+1, j))
#
# 解释:
#     因为左子树高度增加1所以左子树上所有node的高度增加1, 所以向总期望贡献w(i, r-1)
#     因为右子树高度增加1所以右子树上所有node的高度增加1, 所以向总期望贡献w(r+1, j)
#     当前root从无到有, 所以高度也增加1, 向总期望贡献pr
#     所以总的期望增加w(i, j)
#
# 化简得到e[i, j] = e[i, r-1] + e[r+1, j] + w(i, j)


# 选取使得当前二叉树搜索期望最低的方案, 可得最终递归公式：
#
# if j == i - 1:
#     e[i, j] = qi-1
# elif j >= i:
#     e[i, j] = min([(e[i, r-1] + e[r+1, j] + w(i, j)) for r in [i...j]])


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
