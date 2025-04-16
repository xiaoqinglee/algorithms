# https://leetcode.cn/problems/next-greater-element-ii
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:

        # index: nums index
        # val: next bigger num than num[index]
        next_bigger: list[int | None] = [None] * (len(nums) * 2)

        duplicated_num_list: list[int] = nums * 2

        # 单调栈, 自栈底到栈顶严格递减
        # stack element: tuple[num, num_index]
        stack: list[tuple[int, int]] = []
        for i in range(len(duplicated_num_list) - 1, -1, -1):
            if len(stack) == 0 or duplicated_num_list[i] < stack[-1][0]:
                stack.append((duplicated_num_list[i], i))
            else:  # len(stack) != 0 and duplicated_num_list[i] >= stack[-1][0]:
                while len(stack) != 0 and duplicated_num_list[i] >= stack[-1][0]:
                    stack.pop()
                stack.append((duplicated_num_list[i], i))
            if len(stack) >= 2:
                next_bigger[i] = stack[-2][0]
            else:
                next_bigger[i] = -1

        next_bigger = next_bigger[:len(nums)]

        return next_bigger
