class Solution:
    def criticalConnections2(self, n: int, connections: list[tuple[int, int]]) -> list[tuple[int, int]]:

        # DFS 算法

        # 邻接表
        adj: list[list[int]] = [[] for _ in range(n)]
        for edge in connections:
            v1, v2 = edge
            adj[v1].append(v2)
            adj[v2].append(v1)

        result: list[tuple[int, int]] = []

        visited: list[bool] = [False for _ in range(n)]
        dfn: list[int | None] = [None for _ in range(n)]
        low: list[int | None] = [None for _ in range(n)]

        def traverse(v: int, level: int, parent_v: int) -> bool:  # 进行了有效访问返回True否则返回False
            if visited[v] is True:
                return False

            visited[v] = True
            dfn[v] = level
            low[v] = dfn[v]

            # 通过非父子边连接到的祖先节点
            ancestors = [adj_v for adj_v in adj[v] if visited[adj_v] and adj_v != parent_v]
            if len(ancestors) > 0:
                low[v] = min(low[v], min(dfn[ancestor] for ancestor in ancestors))

            # descendants 内的节点在未遍历前不确定哪些是child节点, 哪些是grandchild节点.
            # 我们也可以不在此处筛选visited,
            # 把所有邻接的节点(包括child节点, grandchild节点, parent节点和grandparent节点)全部拿去遍历,
            # 只有traverse()返回true的才是深度优先搜索树上的child节点.
            descendants = [adj_v for adj_v in adj[v] if not visited[adj_v]]

            # child节点
            children = []

            for d in descendants:
                has_made_progress = traverse(d, level+1, v)
                if has_made_progress:
                    children.append(d)

            if len(children) > 0:
                low[v] = min(low[v], min(low[child] for child in children))

            # 此时当前节点的low值已经完全确定
            for child in children:
                if low[child] > dfn[v]:
                    result.append((v, child))

            return True

        traverse(0, 1, -1)

        return result

    def criticalConnections(self, n: int, connections: list[tuple[int, int]]) -> list[tuple[int, int]]:

        # DFS 算法

        # 邻接表
        adj: list[list[int]] = [[] for _ in range(n)]
        for edge in connections:
            v1, v2 = edge
            adj[v1].append(v2)
            adj[v2].append(v1)

        result: list[tuple[int, int]] = []

        visited: list[bool] = [False for _ in range(n)]
        dfn: list[int | None] = [None for _ in range(n)]
        low: list[int | None] = [None for _ in range(n)]

        def traverse(v: int, level: int, parent_v: int) -> bool:  # 进行了有效访问返回True否则返回False
            # 仅在此判断visited
            # [这里必须要判断, 因为不管另一处位置有没有判断, 此处都能遇到visited==True的节点]
            if visited[v] is True:
                return False

            visited[v] = True
            dfn[v] = level
            low[v] = dfn[v]

            # 通过非父子边连接到的祖先节点
            ancestors = [adj_v for adj_v in adj[v] if visited[adj_v] and adj_v != parent_v]
            if len(ancestors) > 0:
                low[v] = min(low[v], min(dfn[ancestor] for ancestor in ancestors))

            # 不在此处筛选visited,
            # 把所有邻接的节点(包括child节点, grandchild节点, parent节点和grandparent节点)全部拿去遍历,
            # 只有traverse()返回true的才是深度优先搜索树上的child节点.
            # [这里判断不判断visited都行, 因为这里不管判断不判断都会让 traverse() 遇到visited==True的节点]
            adj_vs = adj[v]

            # child节点
            children = []

            for adj_v in adj_vs:
                has_made_progress = traverse(adj_v, level+1, v)
                if has_made_progress:
                    children.append(adj_v)

            if len(children) > 0:
                low[v] = min(low[v], min(low[child] for child in children))

            # 此时当前节点的low值已经完全确定
            for child in children:
                if low[child] > dfn[v]:
                    result.append((v, child))

            return True

        traverse(0, 1, -1)

        return result


# 无向图的桥(割边)/割点
#
#
# 在深度优先搜索树中:
# • 时间戳：dfn[u]表示节点u深度优先遍历的序号。
# • 追溯点：low[u]表示节点u或u的子孙能通过非父子边追溯到
# 的dfn最小的节点序号，即回到最早的过去。
#
#
# 1. 无向图的桥
# 桥判定法则： 无向边x-y是桥，当且仅当在搜索树上存在x的一
# 个子节点y时，满足low[y]>dfn[x]。
#
# 也就是说，若孩子的low值比自己的dfn值大，则从该节点到这个孩
# 子的边为桥。
#
# dfn = levelOfDeepFirstTraversal
# low = levelOfOldestAncestorThisNodeCanReach
#
# low是子树的所有叶子节点通过非父子边能连接到的最古老的祖先节点的节点level值, (节点越古老, level越小).
# 孩子的low值比自己的level大, 那么说明这个孩子没有其他途径连接到自己及自己的祖先,
# 此时自己和这个孩子的父子边是桥(割边).
#
# 一个图可能有多个桥(图是单链表), 也可能没有桥(图是环).
#
#
# 2. 无向图的割点
# 割点判定法则： 若x不是根节点，则x是割点，当且仅当在搜索
# 树上存在x的一个子节点y ，满足low[y]≥dfn[x]；若x是根节点，
# 则x是割点，当且仅当在搜索树上至少存在两个子节点，满足该条件。
#
# low[y]==dfn[x] 的例子:
# 1 -> 2 -> 3 -> 4- > 2 中2是割点.


# 有向图和无向图深度优先遍历的区别


# 有向图的深度优先遍历过程中, 当前节点为v, 当前节点的一个邻接点是adj_v,
# adj_v的状态有 0 1 2 三种可能.
#
# 图中的点有三种状态：
# "0": not_finished_and_not_considered
# "1": not_finished_and_being_considered
# "2": finished
#
# 没有遍历前图上的所有节点都是not_finished_and_not_considered状态，
# 向下遍历的时候走过的节点状态变为not_finished_and_being_considered，
# 向上回退的时候节点状态变为finished
#
# 1 状态的adj_v是v的祖先节点.
# 2 状态的adj_v不是v的祖先节点.


# 无向图的深度优先遍历中, 当前节点为v, 当前节点的一个邻接点是adj_v,
# adj_v的状态有 visited not_visited 两种状态.
#
# 如果adj_v的状态是 visited, 那么adj_v一定是v的祖先节点.
# [此时这个连接v和adj_v的边是个父子边(adj_v是v的parent)或非父子边(adj_v是v的grandparent or above)]
#
# 反证法:
#     已经遍历过的所有节点中, 只有祖先节点链上的节点还没有回退完毕, 其他节点都已经回退完毕.
#     假设adj_v不是v的祖先节点, 那么adj_v节点的遍历的回退动作已经执行完毕,
#     因为v与adj_v相互邻接(无向图嘛), 所以adj_v节点的回退前, 必定会等待v节点回退完毕,
#     所以v节点已经回退完毕.
#     v节点回退完毕与当前正在遍历v节点相互矛盾, 所以假设不成立.
