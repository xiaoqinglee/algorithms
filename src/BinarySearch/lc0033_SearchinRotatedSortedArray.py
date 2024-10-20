# https://leetcode.cn/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: list[int], target: int) -> int:

        # 参考 lc 34
        # 首先给数组分段,
        # 右半段是小于等于nums[len(nums)-1]的元素, 左半段是大于nums[len(nums)-1]的元素,
        # 右半段不为空，左半段可能为空.
        # 然后在其中一段上寻找目标值.

        def binary_search_right_half_first_index(lo: int, hi: int) -> int:
            # 返回第一个小于等于nums[len(nums)-1]的元素的索引
            # 当前函数认为array[hi] <= nums[len(nums)-1]
            while True:
                if lo == hi:
                    return lo
                mid = (lo + hi) // 2
                if nums[mid] <= nums[len(nums) - 1]:
                    hi = mid
                else:
                    lo = mid + 1

        def binary_search_target_index(lo: int, hi: int) -> int:
            # 当前函数认为[lo...hi]是个递增序列, 元素各不同
            while True:
                if lo > hi:
                    return -1
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:  # nums[mid] == target
                    return mid

        right_half_first_index: int = binary_search_right_half_first_index(0, len(nums) - 1)
        if target <= nums[len(nums) - 1]:  # 在右半
            return binary_search_target_index(right_half_first_index, len(nums) - 1)
        else:  # 在左半
            return binary_search_target_index(0, right_half_first_index - 1)
