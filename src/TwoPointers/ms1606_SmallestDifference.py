# https://leetcode.cn/problems/smallest-difference-lcci
class Solution:
    def smallestDifference(self, a: list[int], b: list[int]) -> int:
        if len(a) == 0 or len(b) == 0:
            raise "Invalid Input"
        a.sort()
        b.sort()

        min_distance: int | float = float("inf")

        # i in [0...len(a)-1]
        # j in [0...len(b)-1]
        i = j = 0
        while i <= len(a)-1 and j <= len(b)-1:
            if a[i] <= b[j]:
                distance = b[j] - a[i]
                i += 1
            else:
                distance = a[i] - b[j]
                j += 1
            min_distance = min(min_distance, distance)

        return min_distance

    def smallestDifference2(self, a: list[int], b: list[int]) -> int:
        if len(a) == 0 or len(b) == 0:
            raise "Invalid Input"
        # element: tuple[value, value_from_a_list]
        a_and_b: list[tuple[int, bool]] = ([(val, True) for val in a] +
                                           [(val, False) for val in b])
        a_and_b.sort()
        min_distance: int | float = float("inf")
        for i in range(1, len(a_and_b)):
            if a_and_b[i][1] == a_and_b[i-1][1]:
                continue
            else:
                distance = a_and_b[i][0] - a_and_b[i-1][0]
                min_distance = min(min_distance, distance)

        return min_distance
