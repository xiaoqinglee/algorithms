# https://leetcode.cn/problems/minimum-height-trees
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[tuple[int, int]]) -> list[int]:

        v_to_adjacent_vs: dict[int, list[int]] = {}  # 如果一个vertex没有邻接的vertex，那么这个词典中没有这个key
        for v1, v2 in edges:
            if v1 not in v_to_adjacent_vs:
                v_to_adjacent_vs[v1] = []
            v_to_adjacent_vs[v1].append(v2)
            if v2 not in v_to_adjacent_vs:
                v_to_adjacent_vs[v2] = []
            v_to_adjacent_vs[v2].append(v1)

        v_is_visited: dict[int, bool] = {}  # 由上到下走过的node会被认为已经访问过

        def reset_traversal_status_dict() -> None:
            # 给你一棵包含 n 个节点的树，标记为 0 到 n - 1
            for v in range(n):
                v_is_visited[v] = False

        reset_traversal_status_dict()

        def get_unvisited_children(root: int) -> list[int]:
            return [v_ for v_ in v_to_adjacent_vs.get(root, []) if v_is_visited[v_] is False]

        def traverse(root: int) -> int:
            v_is_visited[root] = True
            root_height: int | None = None
            for child in get_unvisited_children(root):
                child_height = traverse(child)
                root_height_candidate = child_height + 1

                # 判断是否及时枝剪掉
                if root_height_candidate > min_height:
                    return root_height_candidate

                if root_height is None:
                    root_height = root_height_candidate
                else:
                    root_height = max(root_height, root_height_candidate)
            return 1 if root_height is None else root_height

        min_height: int = len(v_is_visited)
        root_vertexes: list[int] = []

        for root_vertex_candidate in range(n):
            height = traverse(root_vertex_candidate)
            if height == min_height:
                root_vertexes.append(root_vertex_candidate)
            elif height < min_height:
                min_height = height
                root_vertexes = [root_vertex_candidate]
            else:
                # do nothing
                pass
            reset_traversal_status_dict()

        return root_vertexes
