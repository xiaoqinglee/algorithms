# https://leetcode.cn/problems/two-sum
def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    num_to_index_dict = {}
    for i, num in enumerate(nums):
        # dict中所有的value都是int，所以不存在value为None的key-value pair
        index = num_to_index_dict.get(target - num)
        if index is not None:
            return index, i
        num_to_index_dict[num] = i
    raise "unexpected input"
