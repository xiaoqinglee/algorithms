# https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero
class Solution:
    def minReorder(self, n: int, connections: list[tuple[int, int]]) -> int:

        edges_to_invert: list[tuple[int, int]] = []

        edges_from_this_vertex: dict[int, list[tuple[int, int]]] = {}
        edges_to_this_vertex: dict[int, list[tuple[int, int]]] = {}
        for edge in connections:
            edges_from_this_vertex.setdefault(edge[0], []).append(edge)
            edges_to_this_vertex.setdefault(edge[1], []).append(edge)

        visited_vertexes: set[int] = set()
        vertexes_to_visit_in_this_round = [0]

        while len(vertexes_to_visit_in_this_round) > 0:

            vertexes_to_visit_in_next_round = []
            for v in vertexes_to_visit_in_this_round:
                for edge in edges_from_this_vertex.get(v, []):
                    v_adj = edge[1]
                    if v_adj in visited_vertexes:
                        continue
                    edges_to_invert.append(edge)
                    vertexes_to_visit_in_next_round.append(v_adj)
                for edge in edges_to_this_vertex.get(v, []):
                    v_adj = edge[0]
                    vertexes_to_visit_in_next_round.append(v_adj)
                visited_vertexes.add(v)
            vertexes_to_visit_in_this_round = vertexes_to_visit_in_next_round

        return len(edges_to_invert)
