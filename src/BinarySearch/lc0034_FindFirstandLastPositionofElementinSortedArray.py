# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: list[int], target: int) -> tuple[int, int]:

        # 返回[lo, hi)第一个满足 >= target的元素的索引
        # 函数被调用时, 函数自己的视角: array[hi]满足 >= target
        # 返回值范围[lo...hi]: [lo, hi)内所有元素都满足 -> lo, [lo, hi)内所有元素都不满足 -> hi
        def binary_search_1(lo: int, hi: int) -> int:
            while True:
                if lo == hi:
                    return lo
                mid = (lo + hi) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1

        # 返回[lo, hi)第一个满足 > target的元素的索引
        # 函数被调用时, 函数自己的视角: array[hi]满足 > target
        # 返回值范围[lo...hi]: [lo, hi)内所有元素都满足 -> lo, [lo, hi)内所有元素都不满足 -> hi
        def binary_search_2(lo: int, hi: int) -> int:
            while True:
                if lo == hi:
                    return lo
                mid = (lo + hi) // 2
                if nums[mid] > target:
                    hi = mid
                else:
                    lo = mid + 1

        low_boundary = binary_search_1(0, len(nums))
        high_boundary = binary_search_2(low_boundary, len(nums))

        if low_boundary < high_boundary:
            print("满足条件的子串切片:")
            print(nums[low_boundary:high_boundary])
            return low_boundary, high_boundary - 1
        else:
            return -1, -1