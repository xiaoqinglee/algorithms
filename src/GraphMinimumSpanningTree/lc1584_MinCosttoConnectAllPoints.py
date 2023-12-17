from basics.data_structure.UnionFind import UnionFind


Point = tuple[int, int]


# https://leetcode.cn/problems/min-cost-to-connect-all-points
class Solution:
    def minCostConnectPoints2(self, points: list[Point]) -> int:

        # Kruskal 算法, 时间复杂度ElogV

        # https://en.wikipedia.org/wiki/Kruskal%27s_algorithm#Complexity
        # For a graph with E edges and V vertices, Kruskal's algorithm can be shown to run in O(E log E) time,
        # or equivalently, O(E log V) time, all with simple data structures.

        distance_sum: int = 0
        points = [tuple(p) for p in points]
        sets: UnionFind = UnionFind(from_vertexes=points)

        # distance_and_edge_list 的元素是 tuple[distance, tuple[point1, point2]]
        distance_and_edge_list: list[tuple[int, tuple[Point, Point]]] = []

        for i, (p1_x, p1_y) in enumerate(points):
            for p2_x, p2_y in points[i+1:]:
                distance_and_edge_list.append((abs(p1_x - p2_x) + abs(p1_y - p2_y), ((p1_x, p1_y), (p2_x, p2_y))))

        distance_and_edge_list.sort(key=lambda x: x[0])
        for distance, (p1, p2) in distance_and_edge_list:
            if sets.belongs_to_same_set(p1, p2):
                continue
            sets.union(p1, p2)
            distance_sum += distance

        return distance_sum

    def minCostConnectPoints(self, points: list[Point]) -> int:

        # Prim 算法, 时间复杂度 V^2

        distance_sum: int = 0

        # shortest_edge_to_spanning_tree[v] 表示生成树之外的某个节点 v 到生成树的最短距离
        shortest_edge_to_spanning_tree: list[int | float] = [float("inf")] * len(points)
        # the_other_end_v_on_shortest_edge[v] 表示生成树之外的某个节点 v 到生成树的最短距离边的另一个节点 v', v' 在生成树上
        the_other_end_v_on_shortest_edge: list[int | None] = [None] * len(points)
        # solved_vs 表示生成树上所有的点的集合
        solved_vs: set[int] = set()

        # 随便选择一个起点
        shortest_edge_to_spanning_tree[0] = 0
        the_other_end_v_on_shortest_edge[0] = 0

        for _ in range(len(points)):

            shortest_edge_to_spanning_tree_ = float("inf")
            this_v = None
            for v in range(len(points)):
                if v not in solved_vs and shortest_edge_to_spanning_tree[v] < shortest_edge_to_spanning_tree_:
                    shortest_edge_to_spanning_tree_ = shortest_edge_to_spanning_tree[v]
                    this_v = v

            if shortest_edge_to_spanning_tree_ == float("inf"):
                print("无法找到下一个可以达到的 vertex 了")
                raise "Not enough edge"  # 本题不会出现这种情况, 因为本题中任意两个v之间都有edge
            solved_vs.add(this_v)
            distance_sum += shortest_edge_to_spanning_tree[this_v]

            for adj_v in range(len(points)):  # 松弛所有和this_v邻接的点
                if adj_v in solved_vs:
                    continue

                distance_between_this_v_and_adj_v = \
                    abs(points[this_v][0] - points[adj_v][0]) + abs(points[this_v][1] - points[adj_v][1])

                if distance_between_this_v_and_adj_v == float("inf"):  # this_v -> adj_v 的 edge 不存在, 本题中不会出现这个情况
                    continue

                if distance_between_this_v_and_adj_v < shortest_edge_to_spanning_tree[adj_v]:
                    shortest_edge_to_spanning_tree[adj_v] = distance_between_this_v_and_adj_v
                    the_other_end_v_on_shortest_edge[adj_v] = this_v

        return distance_sum
