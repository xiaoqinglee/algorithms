def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    num_to_index_dict = {}
    for i, num in enumerate(nums):
        index = num_to_index_dict.get(target - num)
        if index is not None:
            return index, i
        num_to_index_dict[num] = i
    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
