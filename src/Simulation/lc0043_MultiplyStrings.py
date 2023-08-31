# https://leetcode.cn/problems/multiply-strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def char_to_int(char: str) -> int:
            return ord(char) - ord("0")

        def int_to_char(int_: int) -> str:
            return chr(ord("0") + int_)

        def multi(char1: str, char2: str) -> int:
            return char_to_int(char1) * char_to_int(char2)

        def produce_digits(int_: int) -> tuple[int, int]:
            high: int = int_ // 10
            low: int = int_ % 10
            return high, low

        result: int = 0

        result_for_this_num2_digit_need_multi_ten_n_times: int = 0
        for num2_index in range(len(num2) - 1, -1, -1):

            num2_digit = num2[num2_index]

            result_for_this_num2_digit: int = 0

            old_high: int = 0
            low_need_multi_ten_n_times: int = 0
            for num1_index in range(len(num1) - 1, -1, -1):
                num1_digit = num1[num1_index]
                high, low = produce_digits(multi(num1_digit, num2_digit) + old_high)
                low = low * (10 ** low_need_multi_ten_n_times)
                result_for_this_num2_digit += low
                old_high = high
                low_need_multi_ten_n_times += 1
            if old_high != 0:
                low = old_high
                low = low * (10 ** low_need_multi_ten_n_times)
                result_for_this_num2_digit += low

            result_for_this_num2_digit = \
                result_for_this_num2_digit * (10 ** result_for_this_num2_digit_need_multi_ten_n_times)

            result += result_for_this_num2_digit

            result_for_this_num2_digit_need_multi_ten_n_times += 1

        result_in_char_list: list[str] = []
        while True:
            high, low = produce_digits(result)
            low_in_char: str = int_to_char(low)
            result_in_char_list.append(low_in_char)
            if high == 0:
                break
            result = high

        result_in_str = "".join(reversed(result_in_char_list))

        return result_in_str
