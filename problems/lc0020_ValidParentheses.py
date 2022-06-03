class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                stack.pop()
            elif char == "[":
                stack.append(char)
            elif char == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                stack.pop()
            elif char == "{":
                stack.append(char)
            elif char == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                stack.pop()
            else:
                raise "Invalid Input s"
        if len(stack) != 0:
            return False
        return True
