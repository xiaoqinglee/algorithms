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
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid

        # 返回[lo, hi)第一个满足 > target的元素的索引
        # 函数被调用时, 函数自己的视角: array[hi]满足 > target
        # 返回值范围[lo...hi]: [lo, hi)内所有元素都满足 -> lo, [lo, hi)内所有元素都不满足 -> hi
        def binary_search_2(lo: int, hi: int) -> int:
            while True:
                if lo == hi:
                    return lo
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid

        low_boundary = binary_search_1(0, len(nums))
        high_boundary = binary_search_2(0, len(nums))
        print("满足条件的子串切片:")
        print(nums[low_boundary:high_boundary])

        return (low_boundary, high_boundary-1) if high_boundary - low_boundary > 0 else (-1, -1)
