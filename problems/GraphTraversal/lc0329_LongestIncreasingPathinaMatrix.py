Point = tuple[int, int]


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        # 最长的递增序列也是最长的递减序列
        # 建立有向图模型, v是matrix中的坐标, 如果一个坐标x上的值比他的某个邻居坐标y上的值大, 那么存在e: x->y
        # 最长递减序列是有向图中最长的path

        # 建立邻接表
        graph: dict[Point, list[Point]] = {}

        def init_graph() -> None:

            def neighbors(position: Point) -> list[Point]:
                x, y = position
                u = x - 1, y
                r = x, y + 1
                d = x + 1, y
                l = x, y - 1
                return [(x, y)
                        for (x, y) in (u, r, d, l)
                        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0])]

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    for neighbor in neighbors((i, j)):
                        if matrix[i][j] > matrix[neighbor[0]][neighbor[1]]:
                            graph.setdefault((i, j), []).append(neighbor)

        init_graph()

        # longest_path[i][j]代表以坐标(i, j)为起点的最长路径的路径长度, 值为None表示该点没有被访问过
        longest_path: list[list[int | None]] = [[None] * len(matrix[0]) for _ in range(len(matrix))]
        # child_v_on_longest_path[i][j]代表以坐标(i, j)为起点的最长路径的路径上下一个v是哪个
        child_v_on_longest_path: list[list[Point | None]] = [[None] * len(matrix[0]) for _ in range(len(matrix))]

        def compute_longest_path(start_point: Point) -> int:
            i, j = start_point
            if longest_path[i][j] is not None:
                return longest_path[i][j]

            adj_points: list[Point] = graph.get(start_point, [])
            longest_path_: int = 0
            child_v_on_longest_path_: Point = None
            if len(adj_points) != 0:
                for adj_point in adj_points:
                    path_len = compute_longest_path(adj_point) + 1
                    if path_len > longest_path_:
                        longest_path_ = path_len
                        child_v_on_longest_path_ = adj_point

            longest_path[i][j] = longest_path_
            child_v_on_longest_path[i][j] = child_v_on_longest_path_
            return longest_path_

        longest_max: int = -float("inf")
        longest_max_start_point_ = None
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest_ = compute_longest_path((i, j))
                if longest_ > longest_max:
                    longest_max = longest_
                    longest_max_start_point_ = (i, j)

        v_on_longest_path: list[int] = []
        point = longest_max_start_point_
        while point is not None:
            v_on_longest_path.append(matrix[point[0]][point[1]])
            point = child_v_on_longest_path[point[0]][point[1]]

        # 代码中表示的path值是edge的数目, 题目要求vertex的数目
        return longest_max + 1


# 课程表拓扑排序问题 "->" 代表依赖
#           p -> q
#                ↓
# a -> b -> c -> x -> y -> z
#
# 递归深度优先遍历过程中,
# 遍历了a的树之后, 不知道下面要访问的元素在依赖图中处在什么位置, 它可能是b/c/x/y/z, 也可能是p/q
