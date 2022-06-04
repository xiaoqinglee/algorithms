class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        # 定义f(i)为所有以i作为最后一个元素的数组中元素之和最大的那个数组的元素之和。
        # f(i) = max(f(i - 1) + nums[i], nums[i])

        if len(nums) == 0:
            return 0

        subarray_right_index: int = 0  # 包含
        subarray_element_value_sum: int = nums[0]
        dp: list[int] = [0] * len(nums)
        dp[subarray_right_index] = subarray_element_value_sum

        max_subarray_right_index: int = subarray_right_index  # 包含
        max_subarray_element_value_sum: int = subarray_element_value_sum

        for i in range(len(nums)):
            if i == 0:
                continue
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            if dp[i] > max_subarray_element_value_sum:
                max_subarray_right_index = i
                max_subarray_element_value_sum = dp[i]

        return max_subarray_element_value_sum
