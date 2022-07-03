class Solution:
    def findWhetherExistsPath(self, n: int, graph: list[list[int]], start: int, target: int) -> bool:
        if start == target:
            return True

        reach_cost_min: list[list[float]] = [[float("inf")] * n for v in range(n)]
        reach_via: list[list[list[int]]] = [[[] for v in range(n)] for v in range(n)]  # 不含起点和终点

        for v1 in range(n):
            for v2 in range(n):
                if v1 == v2:
                    reach_cost_min[v1][v2] = 0.0

        for edge in graph:
            v1, v2 = edge  # 有向图 存在自环
            reach_cost_min[v1][v2] = min(reach_cost_min[v1][v2], 1.0)

        for v1 in range(n):
            for v2 in range(n):
                for v3 in range(n):
                    if v1 == v2 or v1 == v3 or v2 == v3:
                        continue
                    if reach_cost_min[v1][v3] + reach_cost_min[v3][v2] < reach_cost_min[v1][v2]:
                        reach_cost_min[v1][v2] = reach_cost_min[v1][v3] + reach_cost_min[v3][v2]
                        reach_via[v1][v2] = reach_via[v1][v3] + [v3] + reach_via[v3][v2]

        import pprint
        pprint.pprint(reach_cost_min[start][target])
        pprint.pprint(reach_via[start][target])

        return reach_cost_min[start][target] != float("inf")


# Floyd-Warshall algorithm 是解决任意两点间的最短路径的一种算法, 可以正确处理有向图或负权（但不可存在负权回路）的最短路径问题.
# 复杂度 N^3 (N是节点数目)
#
#
# https://zh.wikipedia.org/wiki/最短路问题
# 最短路径问题是图论研究中的一个经典算法问题，旨在寻找图（由结点和路径组成的）中两结点之间的最短路径。算法具体的形式包括：
#
#     确定起点的最短路径问题
#         也叫单源最短路问题，即已知起始结点，求最短路径的问题。
#         在边权非负时适合使用Dijkstra算法，若边权为负时则适合使用Bellman-ford算法或者SPFA算法。
#
#     确定终点的最短路径问题
#         与确定起点的问题相反，该问题是已知终结结点，求最短路径的问题。
#         在无向图中该问题与确定起点的问题完全等同，在有向图中该问题等同于把所有路径方向反转的确定起点的问题。
#
#     确定起点终点的最短路径问题
#         即已知起点和终点，求两结点之间的最短路径。
#
#     全局最短路径问题
#         也叫多源最短路问题，求图中所有的最短路径。适合使用Floyd-Warshall算法。
