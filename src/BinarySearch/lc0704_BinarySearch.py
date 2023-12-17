# https://leetcode.cn/problems/binary-search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        def first_greater_than_or_equal_to(lo: int, hi: int) -> int:
            while True:
                if lo == hi:
                    return lo
                mid = (lo + hi) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1

        possible_index = first_greater_than_or_equal_to(0, len(nums))
        if possible_index <= len(nums) - 1:
            if nums[possible_index] == target:
                return possible_index
            else:
                return -1
        else:  # possible_index == len(nums)
            return -1
