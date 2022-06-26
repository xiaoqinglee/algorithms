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
