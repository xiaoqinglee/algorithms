class Solution:
    def findWhetherExistsPath(self, n: int, graph: list[list[int]], start: int, target: int) -> bool:
        if start == target:
            return True

        # v1 != v2,
        # 从v1到v2的最短路径长度是reach_cost_min[v1][v2]的值, 是len(reach_via[v1][v2]) + 1.
        # len(reach_via[v1][v2]) + 2 是包含起点和终点路径上所有的节点数.
        reach_cost_min: list[list[int | float]] = [[float("inf")] * n for v in range(n)]
        reach_via: list[list[list[int]]] = [[[] for v in range(n)] for v in range(n)]  # 不含起点和终点

        for edge in graph:
            v1, v2 = edge
            if v1 == v2:  # 有向图存在平行边存在自环, 我们要排除这些干扰, 将图转换为没有平行边的有向无环图
                continue
            reach_cost_min[v1][v2] = min(reach_cost_min[v1][v2], 1)

        for v1 in range(n):
            for v2 in range(n):
                for v3 in range(n):
                    if v1 == v2 or v1 == v3 or v2 == v3:
                        continue
                    if reach_cost_min[v1][v3] + reach_cost_min[v3][v2] < reach_cost_min[v1][v2]:
                        reach_cost_min[v1][v2] = reach_cost_min[v1][v3] + reach_cost_min[v3][v2]
                        reach_via[v1][v2] = reach_via[v1][v3] + [v3] + reach_via[v3][v2]

        # import pprint
        # pprint.pprint(reach_cost_min[start][target])
        # pprint.pprint(reach_via[start][target])

        return reach_cost_min[start][target] != float("inf")


# Floyd-Warshall algorithm 是解决任意两点间的最短路径的一种算法, 可以正确处理有向图或负权（但不可存在负权回路）的最短路径问题.
# 复杂度 N^3 (N是节点数目)
#
#
# https://zh.wikipedia.org/wiki/最短路问题
# 最短路径问题是图论研究中的一个经典算法问题，旨在寻找图（由结点和路径组成的）中两结点之间的最短路径。算法具体的形式包括：
#
#     确定起点的最短路径问题(Single-destination shortest-paths problem)
#         也叫单源最短路问题，即已知起始结点，求最短路径的问题。
#         在边权非负时适合使用Dijkstra算法，若边权为负时则适合使用Bellman-ford算法或者SPFA算法。
#
#     确定终点的最短路径问题
#         与确定起点的问题相反，该问题是已知终结结点，求最短路径的问题。
#         在无向图中该问题与确定起点的问题完全等同，在有向图中该问题等同于把所有路径方向反转的确定起点的问题。
#
#     确定起点终点的最短路径问题(Single-pair shortest-path problem)
#         即已知起点和终点，求两结点之间的最短路径。
#         Introduction to Algorithms 4ed:
#             Find a shortest path from u to v for
#             given vertices u and v. If you solve the single-source problem with
#             source vertex u, you solve this problem also. Moreover, all known
#             algorithms for this problem have the same worst-case asymptotic
#             running time as the best single-source algorithms.
#         如果我们能找到一个有效的 heuristic function, 可以使用 A* 搜索.
#
#     全局最短路径问题(All-pairs shortest-paths problem)
#         也叫多源最短路问题，求图中所有的最短路径。适合使用Floyd-Warshall算法。
