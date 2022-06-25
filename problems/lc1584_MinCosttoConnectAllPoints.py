from math import sqrt

from basics.data_structure.UnionFind import UnionFind


class Solution:
    def minCostConnectPoints(self, points: list[tuple[int, int]]) -> int:

        distance_sum: int = 0
        points = [tuple(p) for p in points]
        sets: UnionFind = UnionFind(from_vertexes=points)

        # dict 已经具备OrderedDict的key写入与读出顺序一致的特性
        distance_to_point_pairs: dict[int, list[tuple[tuple[int, int], tuple[int, int]]]] = {}

        for i, (p1_x, p1_y) in enumerate(points):
            for p2_x, p2_y in points[i+1:]:
                distance_to_point_pairs.setdefault(abs(p1_x - p2_x) + abs(p1_y - p2_y),
                                                  []).append(((p1_x, p1_y), (p2_x, p2_y)))

        distance_to_point_pairs = {k: distance_to_point_pairs[k] for k in sorted([x for x in distance_to_point_pairs])}
        for distance, point_pairs in distance_to_point_pairs.items():
            for p1, p2 in point_pairs:
                if sets.belongs_to_same_set(p1, p2):
                    continue
                sets.union(p1, p2)
                distance_sum += distance

        return distance_sum
