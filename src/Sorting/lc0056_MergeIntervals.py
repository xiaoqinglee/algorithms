# https://leetcode.cn/problems/merge-intervals
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        merged: list[list[int]] = []
        for i, interval in enumerate(intervals):
            if i == 0:
                merged.append(interval)
            else:
                if interval[0] <= merged[-1][1]:
                    merged[-1][1] = max(merged[-1][1], interval[1])
                else:
                    merged.append(interval)
        return merged
