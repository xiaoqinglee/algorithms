from functools import cmp_to_key


# https://leetcode.cn/problems/largest-number
class Solution:

    # [21, 2] -> 221
    # [23, 2] -> 232

    def largestNumber(self, nums: list[int]) -> str:
        if all((x == 0 for x in nums)):  # 一定要使用生成器推导式而不是列表推导式
            return "0"

        nums_in_str: list[str] = list(map(str, nums))

        def cmp(left: str, right: str) -> int:
            prefix: int = min(len(left), len(right))
            if left[:prefix] > right[:prefix]:
                return -1
            elif left[:prefix] < right[:prefix]:
                return 1
            else:
                if len(left) > len(right):
                    return cmp(left[prefix:], right)
                elif len(left) < len(right):
                    return cmp(left, right[prefix:])
                else:
                    return 0

        nums_in_str.sort(key=cmp_to_key(cmp))
        return "".join(nums_in_str)
