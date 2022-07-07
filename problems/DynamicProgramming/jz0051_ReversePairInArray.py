class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        # # 应对 leetcode极端测试用例: 升序超大数组
        # import random
        # random.shuffle(nums)

        if len(nums) == 0:
            return 0

        answer: int = 0

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
                    nonlocal answer
                    answer += (mid_index - left_pointer + 1)
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

        sort_top_down(0, len(nums) - 1)

        return answer
