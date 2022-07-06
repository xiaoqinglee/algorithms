class Solution:
    def findWhetherExistsPath2(self, n: int, graph: list[list[int]], start: int, target: int) -> bool:
        if start == target:
            return True

        # Floyd 算法, 时间复杂度V^3

        # v1 != v2,
        # 从v1到v2的最短路径长度是reach_cost_min[v1][v2]的值, 是len(reach_via[v1][v2]) + 1.
        # len(reach_via[v1][v2]) + 2 是包含起点和终点路径上所有的节点数.
        reach_cost_min: list[list[int | float]] = [[float("inf")] * n for v in range(n)]
        reach_via: list[list[list[int]]] = [[[] for v in range(n)] for v in range(n)]  # 不含起点和终点

        for edge in graph:  # 存在平行边和自环, 我们要排除这些干扰
            v1, v2 = edge
            if v1 == v2:
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

    def findWhetherExistsPath(self, n: int, graph: list[list[int]], start: int, target: int) -> bool:
        if start == target:
            return True

        # BFS 算法, 时间复杂度E+V

        # 无权重的有向无环或有环图的单源最短路径问题可以使用广度优先遍历,
        # 如果是确定起点终点的最短路径问题那么我们可以在找到终点后提前停下来

        adj_vs: dict[int, set[int]] = {}
        visited: dict[int, bool] = {}
        length_of_shortest_path: dict[int, int] = {}
        prev_v_on_shortest_path: dict[int, int] = {}

        for v in range(n):
            visited[v] = False

        for edge in graph:  # 存在平行边和自环, 我们要排除这些干扰
            v1, v2 = edge
            if v1 == v2:
                continue
            adj_vs.setdefault(v1, set()).add(v2)

        from collections import deque
        # v_pairs 的元素是 tuple[v, prev]
        v_pairs: deque[tuple[int, int]] = deque()
        v_pairs.append((start, start))

        length: int = 0
        n_vs_in_this_round: int = 1
        while len(v_pairs) > 0:

            for i in range(n_vs_in_this_round):
                v, prev = v_pairs.popleft()
                # 仅在此处判断visited
                # [这里必须要判断, 因为不管另一处位置有没有判断, 此处都能遇到visited==True的节点]
                if visited[v] is True:
                    continue
                print("visit v", v)
                visited[v] = True
                length_of_shortest_path[v] = length
                prev_v_on_shortest_path[v] = prev
                # 不能只在此处判断visited, 因为这样做后仍然可能会让同一个visited==False的node入队两次
                # [这里判断不判断visited都行, 因为这里不管判断不判断都会让真正访问时遇到visited==True的节点]
                for adj_v in adj_vs.get(v, set()):
                    v_pairs.append((adj_v, v))

            length += 1
            n_vs_in_this_round = len(v_pairs)

        if visited[target]:
            print("存在可行解.")
            print("从起点到终点的 length:", length_of_shortest_path[target])

            nodes_on_path: list[int] = []
            node = target
            while node != start:
                nodes_on_path.append(node)
                node = prev_v_on_shortest_path[node]
            nodes_on_path.append(node)
            nodes_on_path.reverse()
            print("从起点到终点的路径:", nodes_on_path)

        return visited[target]


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
#         如果我们能找到一个有效的 heuristic function, 可以使用 A* 搜索算法高效地寻找近似最短路径.
#
#     全局最短路径问题(All-pairs shortest-paths problem)
#         也叫多源最短路问题，求图中任意两点间的最短路径。
#         适合使用Floyd-Warshall算法, 它可以正确处理有向图或负权（但不可存在负权回路）的最短路径问题。
