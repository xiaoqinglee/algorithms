# https://leetcode.cn/problems/merge-sorted-array/


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        assert m <= len(nums1)
        assert n == len(nums2)
        assert m + n == len(nums1)

        num1_idx_to_read = m - 1
        num2_idx_to_read = n - 1
        num1_idx_to_write = m + n - 1
        while True:
            if nums1[num1_idx_to_read] > nums2[num2_idx_to_read]:
                nums1[num1_idx_to_write] = nums1[num1_idx_to_read]
                num1_idx_to_read -= 1
            else:
                nums1[num1_idx_to_write] = nums2[num2_idx_to_read]
                num2_idx_to_read -= 1
            num1_idx_to_write -= 1
            if num1_idx_to_read < 0 or num2_idx_to_read < 0:
                break
        if num2_idx_to_read >= 0:
            nums1[:num2_idx_to_read + 1] = nums2[:num2_idx_to_read + 1]
        if num1_idx_to_read >= 0:
            pass
