Char = str


# https://leetcode.cn/problems/longest-valid-parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        max_len: int = 0

        # stack element: tuple[char, char_index]
        stack: list[tuple[Char, int]] = []

        for i, char in enumerate(s):
            if char == "(":
                stack.append((char, i))
            elif char == ")":
                if len(stack) == 0 or stack[-1][0] != "(":
                    stack.append((char, i))
                else:  # stack[-1][0] == "("
                    stack.pop()
                    length = i - (stack[-1][1] if len(stack) > 0 else -1)
                    max_len = max(length, max_len)
            else:
                raise "Invalid Input"

        return max_len
