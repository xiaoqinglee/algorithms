# https://leetcode.cn/problems/trapping-rain-water/
class Solution:
    def trap(self, height: list[int]) -> int:

        max_height_to_the_right: list[int] = height.copy()
        for i in range(len(height) - 2, -1, -1):
            max_height_to_the_right[i] = max(max_height_to_the_right[i], max_height_to_the_right[i + 1])

        max_height_to_the_left: list[int] = height.copy()
        for i in range(1, len(height)):
            max_height_to_the_left[i] = max(max_height_to_the_left[i - 1], max_height_to_the_left[i])

        area_sum: int = 0
        for i in range(len(height)):
            area = 1 * (min(max_height_to_the_right[i], max_height_to_the_left[i]) - height[i])
            area_sum += area

        return area_sum
