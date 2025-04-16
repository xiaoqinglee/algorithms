# https://leetcode.cn/problems/daily-temperatures
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        # 从右向左遍历temperatures，将较高的温度的元素放在栈底，保持栈单调. 栈元素是二元组(temperature, day_index)
        higher_temperatures_in_future: list[tuple[int, int]] = []

        result: list[int | None] = [None] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while len(higher_temperatures_in_future) > 0 and not temperatures[i] < higher_temperatures_in_future[-1][0]:
                higher_temperatures_in_future.pop()
            if len(higher_temperatures_in_future) == 0:
                result[i] = 0
            else:
                result[i] = higher_temperatures_in_future[-1][1] - i
            higher_temperatures_in_future.append((temperatures[i], i))

        return result
