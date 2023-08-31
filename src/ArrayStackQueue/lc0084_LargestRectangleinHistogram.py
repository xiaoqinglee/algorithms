# https://leetcode.cn/problems/largest-rectangle-in-histogram
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        # index为i处高度为heights[i]
        # 尝试画一个包含heights[i]且高度为heights[i]的矩形
        # i左侧第一个满足heights[l] < heights[i]的元素 l 是矩形的左边界(不包含)
        # i右侧第一个满足heights[r] < heights[i]的元素 r 是矩形的右边界(不包含)
        # 矩形的底是[l+1...r-1]

        # 构建一个自栈底到栈顶元素严格递增的单调栈,
        # a元素入栈导致b元素(heights[i])被挤出, 那么a元素就是i右侧第一个小于heights[i]的元素heights[r]
        # b出栈时(或b入栈时)b在该单调栈相邻的左侧元素就是在原数组中左侧第一个小于heights[i]的元素heights[l]
        # stack 元素 tuple[height, height_index]
        stack: list[tuple[int, int]] = []

        # 小技巧在原数组尾部追加一个0元素, 让最终的严格递增栈逐步弹空
        heights.append(0)

        max_area: int = 0
        for i, height in enumerate(heights):
            if len(stack) == 0 or stack[-1][0] < height:
                stack.append((height, i))
            else:  # len(stack) != 0 and stack[-1][0] >= height
                while len(stack) != 0 and stack[-1][0] >= height:
                    # rectangle_width = (r-1) - (l+1) + 1
                    rectangle_width = (i-1) - (stack[-2][1] + 1 if len(stack) >= 2 else 0) + 1
                    area = rectangle_width * stack[-1][0]
                    max_area = max(area, max_area)
                    stack.pop()
                stack.append((height, i))

        return max_area
