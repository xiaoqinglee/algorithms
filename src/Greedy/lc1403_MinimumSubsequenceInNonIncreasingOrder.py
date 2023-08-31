# https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order
class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums = sorted(nums, reverse=True)
        sum_= 0
        sum_of_the_rest= sum(nums)
        for i, num in enumerate(nums):
            sum_ += num
            sum_of_the_rest -= num
            if sum_ > sum_of_the_rest:
                return nums[:i+1]
