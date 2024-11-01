# https://leetcode.cn/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # # 应对 leetcode极端测试用例: 升序超大数组
        # import random
        # random.shuffle(nums)

        if k > len(nums):
            raise "Invalid Input"

        # 如果数组长度为10， 如果想要选择第3大的元素，那么数组从小大排序后这个元素所在的位置是索引7
        target_value = quick_select(nums, 0, len(nums) - 1, len(nums) - k)
        return target_value


# left_index（包含），right_index（包含）
def quick_select(nums: list[int], left_index: int, right_index: int, target_index: int) -> int:
    if left_index == right_index:
        return nums[left_index]

    left_pointer, right_pointer = left_index, right_index

    # 要求左指针掠过的值小于标兵，所以标兵所在的初始位置是个坑，而且是待填的第一个坑，
    # 所以先移动右指针。
    # 最后把标兵的值填充到中间的坑里。
    # 同一时刻仅有一个坑位。
    # 遇到坏元素停下来挖出来填到对方的坑里，然后换对方指针移动来填我的坑。
    to_compare_with = nums[left_pointer]
    while True:
        while left_pointer < right_pointer and to_compare_with <= nums[right_pointer]:
            right_pointer -= 1
        if left_pointer == right_pointer:
            break
        nums[left_pointer] = nums[right_pointer]
        left_pointer += 1
        while left_pointer < right_pointer and nums[left_pointer] < to_compare_with:
            left_pointer += 1
        if left_pointer == right_pointer:
            break
        nums[right_pointer] = nums[left_pointer]
        right_pointer -= 1
    assert left_pointer == right_pointer
    nums[left_pointer] = to_compare_with

    if target_index <= left_pointer:
        return quick_select(nums, left_index, left_pointer, target_index)
    else:
        return quick_select(nums, left_pointer + 1, right_index, target_index)


# 时间复杂度：O(n)，证明过程可以参考「《算法导论》9.2：期望为线性的选择算法」。
# 空间复杂度：O(logn)，递归使用栈空间的空间代价的期望为 O(logn)。