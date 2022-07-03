class Solution:

    def decodeString(self, s: str) -> str:

        # 使用两个栈，一个存放整数元素，一个存放单个字符元素和 "[" 符号，
        # 遇到一个"]"符号时，弹出整数栈栈顶元素n， 弹出一个和多个字符栈栈顶元素，直到最后一个弹出的元素是 "["，
        # 把字符串重复n遍的结果(即"[]"展开的结果)逐一放入栈顶，不含"["。
        # 最终的结果就是字符栈的顺序遍历结果。

        char_stack: list[str] = []
        int_stack: list[int] = []

        def is_digit_char(digit: str) -> bool:
            return ord("0") <= ord(digit) <= ord("9")

        current_integer: int = 0
        current_sub_string: list[str] = []

        for char in s:
            if is_digit_char(char):
                current_integer = current_integer * 10 + (ord(char) - ord("0"))
            elif char == "[":
                int_stack.append(current_integer)
                current_integer = 0
                char_stack.append(char)
            elif char == "]":
                current_sub_string = []
                while char_stack[-1] != "[":
                    current_sub_string.append(char_stack[-1])
                    char_stack.pop()
                # assert len(char_stack) > 0 and char_stack[-1] == "["
                char_stack.pop()
                repeat_n_times: int = int_stack[-1]
                int_stack.pop()
                for _ in range(repeat_n_times):
                    for i in range(len(current_sub_string) - 1, -1, -1):
                        char_stack.append(current_sub_string[i])
            else:  # 普通的字母字符
                char_stack.append(char)

        return "".join(char_stack)
