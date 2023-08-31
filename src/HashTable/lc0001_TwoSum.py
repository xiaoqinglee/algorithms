# https://leetcode.cn/problems/two-sum
def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    num_to_index_dict = {}
    for i, num in enumerate(nums):
        # dict中所有的value都是int，所以不存在value为None的key-value pair
        index = num_to_index_dict.get(target - num)
        if index is not None:
            return index, i
        num_to_index_dict[num] = i
    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
