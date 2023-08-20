from collections.abc import Generator


class Solution:
    def isHappy(self, n: int) -> bool:

        def digits(num: int) -> Generator[int, None, None]:
            while True:
                if num <= 0:
                    break
                num, digit = divmod(num, 10)
                yield digit
            return None

        seen: set[int] = set()
        while True:
            if n in seen:
                return False
            sum_ = sum(digit ** 2 for digit in digits(n))
            if sum_ == 1:
                return True
            seen.add(n)
            n = sum_
