Char = str


# https://leetcode.cn/problems/longest-valid-parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        max_len: int = 0

        # stack element: tuple[char, char_index]
        stack: list[tuple[Char, int]] = []

        for i, char in enumerate(s):
            if char == ")" and (len(stack) > 0 and stack[-1][0] == "("):
                stack.pop()
                length = i - (stack[-1][1] if len(stack) > 0 else -1)
                max_len = max(length, max_len)
            else:
                stack.append((char, i))

        return max_len
