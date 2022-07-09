from collections.abc import Callable


def merge_sort(nums: list[int], key: Callable[[int], int] = lambda x: x) -> list[int]:
    # # 应对 leetcode极端测试用例: 升序超大数组
    # import random
    # random.shuffle(nums)

    if len(nums) == 0:
        return nums

    container: list[int] = nums.copy()

    def merge(left: int, mid: int, right: int) -> None:
        # 归并数组 nums[left...mid] 和 nums[mid+1...right]
        container[left:right + 1] = nums[left: right + 1]
        left_pointer = left
        right_pointer = mid + 1
        merging_pointer = left
        while left_pointer <= mid and right_pointer <= right:
            if key(container[left_pointer]) <= key(container[right_pointer]):
                nums[merging_pointer] = container[left_pointer]
                left_pointer += 1
            else:
                nums[merging_pointer] = container[right_pointer]
                right_pointer += 1
            merging_pointer += 1
        while left_pointer <= mid:
            nums[merging_pointer] = container[left_pointer]
            left_pointer += 1
            merging_pointer += 1
        while right_pointer <= right:
            nums[merging_pointer] = container[right_pointer]
            right_pointer += 1
            merging_pointer += 1

    def sort_top_down(left: int, right: int) -> None:  # 自顶向下
        if left >= right:
            return
        mid = (left + right) // 2
        sort_top_down(left, mid)
        sort_top_down(mid + 1, right)
        merge(left, mid, right)

    def sort_bottom_up() -> None:  # 自底向上

        subarray_size = 1
        while subarray_size <= len(nums)-1:

            left = 0
            while left + subarray_size <= len(nums) - 1:
                merge(left, left + subarray_size - 1,
                      min(left + subarray_size * 2 - 1, len(nums) - 1))
                left += (subarray_size * 2)

            subarray_size *= 2

    # sort_top_down(0, len(nums) - 1)
    sort_bottom_up()
    return nums
