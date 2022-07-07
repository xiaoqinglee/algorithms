def three_sum(nums: list[int]) -> list[tuple[int, int, int]]:
    # 三个指针，每个指针只处理运动方向上第一个数值，后面重复的数值会被忽略

    result: list[tuple[int, int, int]] = []
    if len(nums) < 3:
        return result

    nums.sort()

    left_pointer = -1
    while True:
        # 移动左指针
        left_pointer += 1
        # 注意第一个元素
        while 1 <= left_pointer <= len(nums) - 1 and nums[left_pointer] == nums[left_pointer - 1]:
            left_pointer += 1
        if left_pointer > len(nums) - 3:
            break

        mid_pointer = left_pointer + 1
        right_pointer = len(nums) - 1
        while True:
            if nums[left_pointer] + nums[mid_pointer] + nums[right_pointer] == 0:
                result.append((nums[left_pointer], nums[mid_pointer], nums[right_pointer]))
                # 两个指针都移动
                mid_pointer += 1
                while mid_pointer < right_pointer and nums[mid_pointer] == nums[mid_pointer - 1]:
                    mid_pointer += 1
                right_pointer -= 1
                while mid_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]:
                    right_pointer -= 1
            elif nums[left_pointer] + nums[mid_pointer] + nums[right_pointer] < 0:
                # 移动右侧指针
                mid_pointer += 1
                while mid_pointer < right_pointer and nums[mid_pointer] == nums[mid_pointer - 1]:
                    mid_pointer += 1
            else:  # nums[left_pointer] + nums[mid_pointer] + nums[right_pointer] > 0
                # 移动中间指针
                right_pointer -= 1
                while mid_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]:
                    right_pointer -= 1
            if mid_pointer >= right_pointer:
                break

    return result
