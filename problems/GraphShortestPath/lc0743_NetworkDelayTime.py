from pprint import pprint


class Solution:
    def networkDelayTime(self, times: list[tuple[int, int, int]], n: int, k: int) -> int:

        # 权重非负的有向无环或有环图的单源最短路径问题, 使用 Dijkstra 算法

        # 本题目v的标号从1开始
        time_matrix: list[list[int | float]] = [[float("inf")] * (n + 1) for i in range(n + 1)]
        for v1, v2, time in times:
            time_matrix[v1][v2] = time

        shortest_path_from_source: list[int | float] = [float("inf")] * (n + 1)
        prev_v_on_shortest_path: list[int | None] = [None] * (n + 1)
        solved_vs: set[int] = set()

        shortest_path_from_source[k] = 0
        prev_v_on_shortest_path[k] = k

        for _ in range(n):

            shortest_path_to_source_ = float("inf")
            this_v = None
            for v in range(1, n+1):
                if v not in solved_vs and shortest_path_from_source[v] < shortest_path_to_source_:
                    shortest_path_to_source_ = shortest_path_from_source[v]
                    this_v = v

            if shortest_path_to_source_ == float("inf"):
                print("无法找到下一个可以达到的 vertex 了")
                return -1
            solved_vs.add(this_v)

            for adj_v, time in enumerate(time_matrix[this_v]):
                if adj_v == 0:  # v的标号不存在
                    continue
                if adj_v in solved_vs:  # Dijkstra 可以用于有环图 https://www.zhihu.com/question/61830552
                    continue
                if time == float("inf"):  # this_v -> adj_v 的 edge 不存在
                    continue
                # time_matrix[this_v][adj_v] 就是 time
                if shortest_path_from_source[this_v] + time_matrix[this_v][adj_v] < shortest_path_from_source[adj_v]:
                    shortest_path_from_source[adj_v] = shortest_path_from_source[this_v] + time_matrix[this_v][adj_v]
                    prev_v_on_shortest_path[adj_v] = this_v

        path_for_each_target: dict[int, list[int]] = {}
        for target in range(1, n+1):

            nodes_on_path: list[int] = []
            node = target
            while node != k:
                nodes_on_path.append(node)
                node = prev_v_on_shortest_path[node]
            nodes_on_path.append(node)
            nodes_on_path.reverse()

            path_for_each_target[target] = nodes_on_path

        pprint("从起点到各个终点走过的节点:")
        pprint(path_for_each_target)

        pprint("从起点到各个终点的路径长度:")
        pprint(shortest_path_from_source[1:])

        return max(shortest_path_from_source[1:])
