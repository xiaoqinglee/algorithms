# https://leetcode.cn/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        right_to_left = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack: list[str] = []
        for char in s:
            if char in right_to_left.values():
                stack.append(char)
            elif char in right_to_left:
                left = right_to_left[char]
                if not (len(stack) > 0 and stack[-1] == left):
                    return False
                stack.pop()
            else:
                raise "Invalid Input s"
        if len(stack) != 0:
            return False
        return True
