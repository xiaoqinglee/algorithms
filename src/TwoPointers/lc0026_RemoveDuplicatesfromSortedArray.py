# https://leetcode.cn/problems/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            raise "Invalid Input"
        if len(nums) == 1:
            return 1

        writing_pointer = 0  # 指向已经写入的最后一个元素
        reading_pointer = 1  # 指向即将要读取的元素
        while True:
            if nums[reading_pointer] != nums[writing_pointer]:
                writing_pointer += 1
                nums[writing_pointer] = nums[reading_pointer]
            reading_pointer += 1
            if reading_pointer > len(nums) - 1:
                break
        return writing_pointer + 1
