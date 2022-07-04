from math import sqrt
from basics.data_structure.UnionFind import UnionFind


Point = tuple[int, int]


class Solution:
    def minCostConnectPoints(self, points: list[Point]) -> int:

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
