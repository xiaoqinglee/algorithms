# https://leetcode.cn/problems/container-with-most-water
def container_with_most_water(height: list[int]) -> int:
    if len(height) <= 1:
        raise "Invalid Input height"
    left_index = 0
    right_index = len(height) - 1
    max_area = 0
    while True:
        if left_index == right_index:
            break
        area = (right_index - left_index) * min(height[left_index], height[right_index])
        max_area = area if area > max_area else max_area
        if height[left_index] < height[right_index]:
            left_index += 1
        else:
            right_index -= 1
    return max_area
