# https://leetcode.cn/problems/largest-rectangle-in-histogram
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        # 想象 input [1, 5, 4, 3, 2, 3, 4, 5, 6, 7, 1]。 input[4] 被弹出时，画一个底包含 index 4， 高为 input[4] 2 的矩形。

        # index为i处高度为heights[i]
        # 在heights[i]被弹出时，画一个底包含i且高度为heights[i]的矩形
        # i左侧第一个满足 heights[l] < heights[i] 的索引 l 是矩形的左边界(不包含)
        # i右侧第一个满足 heights[i] > heights[r] 的索引 r 是矩形的右边界(不包含)
        # 矩形的底是[l+1...r-1]

        # 构建一个自栈底到栈顶元素严格递增的单调栈,
        # heights[i] 出栈时(或 heights[i] 入栈时) 它在该单调栈相邻的左侧元素就是 heights[l]
        # 当且仅当 heights[r] 元素入栈导致 heights[i] 元素被挤出

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
