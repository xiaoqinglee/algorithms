def merge_sort(nums: list[int]) -> list[int]:
    # # 应对 leetcode极端测试用例: 升序超大数组
    # import random
    # random.shuffle(nums)

    if len(nums) == 0:
        return nums

    container: list[int] = nums.copy()

    def merge(left_index: int, mid_index: int, right_index: int) -> None:
        # 归并数组 nums[left_index..mid_index] 和 nums[mid_index+1..right_index]
        container[left_index:right_index + 1] = nums[left_index: right_index + 1]
        left_pointer = left_index
        right_pointer = mid_index + 1
        merging_pointer = left_index
        while left_pointer <= mid_index and right_pointer <= right_index:
            if container[left_pointer] <= container[right_pointer]:
                nums[merging_pointer] = container[left_pointer]
                left_pointer += 1
            else:
                nums[merging_pointer] = container[right_pointer]
                right_pointer += 1
            merging_pointer += 1
        while left_pointer <= mid_index:
            nums[merging_pointer] = container[left_pointer]
            left_pointer += 1
            merging_pointer += 1
        while right_pointer <= right_index:
            nums[merging_pointer] = container[right_pointer]
            right_pointer += 1
            merging_pointer += 1

    def sort_top_down(left_index: int, right_index: int) -> None:  # 自顶向下
        if left_index >= right_index:
            return
        mid = (left_index + right_index) // 2
        sort_top_down(left_index, mid)
        sort_top_down(mid+1, right_index)
        merge(left_index, mid, right_index)

    def sort_bottom_up() -> None:  # 自底向上

        subarray_size = 1
        while subarray_size <= len(nums)-1:

            left_index = 0
            while left_index + subarray_size <= len(nums) - 1:
                merge(left_index, left_index + subarray_size - 1,
                      min(left_index + subarray_size * 2 - 1, len(nums) - 1))
                left_index += (subarray_size * 2)

            subarray_size *= 2

    # sort_top_down(0, len(nums) - 1)
    sort_bottom_up()
    return nums

