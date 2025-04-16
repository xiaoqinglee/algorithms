# https://leetcode.cn/problems/next-greater-element-i
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # 寻找的相对于 x 下一个更 * 的元素 y 总是在单调栈新元素入栈稳定后次栈顶的位置, x 在栈顶, y 在次栈顶.

        # key: num
        # val: next bigger one than num
        next_bigger: dict[int, int] = {}

        # 单调栈, 自栈底到栈顶严格递减
        stack: list[int] = []
        for i in range(len(nums2) - 1, -1, -1):
            if len(stack) == 0 or nums2[i] < stack[-1]:
                stack.append(nums2[i])
            else:  # len(stack) != 0 and  nums2[i] >= stack[-1]:
                while len(stack) != 0 and nums2[i] >= stack[-1]:
                    stack.pop()
                stack.append(nums2[i])
            if len(stack) >= 2:
                next_bigger[nums2[i]] = stack[-2]
            else:
                next_bigger[nums2[i]] = -1

        return [next_bigger[num] for num in nums1]
