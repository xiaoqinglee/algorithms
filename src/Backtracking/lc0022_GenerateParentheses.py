# https://leetcode.cn/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result: list[str] = []
        char_list: list[str | None] = [None] * (n * 2)

        def back_trace(fixed_first_n_chars: int, remaining_left: int, remaining_right: int):
            if fixed_first_n_chars == n * 2:
                result.append("".join(char_list))
                return
            if remaining_left > 0:
                char_list[fixed_first_n_chars] = "("
                back_trace(fixed_first_n_chars + 1, remaining_left - 1, remaining_right)
                char_list[fixed_first_n_chars] = None
            if remaining_left < remaining_right:
                char_list[fixed_first_n_chars] = ")"
                back_trace(fixed_first_n_chars + 1, remaining_left, remaining_right - 1)
                char_list[fixed_first_n_chars] = None
        back_trace(0, n, n)
        return result
