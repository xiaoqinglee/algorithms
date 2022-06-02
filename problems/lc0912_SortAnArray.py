# https://www.cnblogs.com/curo0119/p/8588565.html

def quick_sort(nums: list[int]) -> list[int]:
    # # 应对 leetcode极端测试用例: 升序超大数组
    # import random
    # random.shuffle(nums)

    if len(nums) == 0:
        return nums

    # left_index（包含），right_index（包含）
    def partition(left_index: int, right_index: int) -> int:
        assert left_index < right_index

        left_pointer, right_pointer = left_index, right_index

        # 要求左指针略过的值小于标兵，所以标兵所在的初始位置是个坑，而且是待填的第一个坑，
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
        return left_pointer

    def sort(left_index: int, right_index: int) -> None:
        if left_index >= right_index:
            return
        mid_index = partition(left_index, right_index)
        sort(left_index, mid_index - 1)
        sort(mid_index + 1, right_index)

    sort(0, len(nums) - 1)
    return nums
