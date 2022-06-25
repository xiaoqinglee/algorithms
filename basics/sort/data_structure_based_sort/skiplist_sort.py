import random


def skiplist_sort(nums: list[int]) -> list[int]:
    # # 应对 leetcode极端测试用例: 升序超大数组
    # import random
    # random.shuffle(nums)

    if len(nums) == 0:
        return nums

    sorted_ = []
    from basics.data_structure.RedisZset import ZSet
    zset: ZSet = ZSet(elem_to_score={
        random.uniform(0, 4200).hex(): score for score in nums
    })
    list_node = zset.skiplist.dummy_header.levels[0].forward
    while list_node is not None:
        sorted_.append(list_node.score)
        list_node = list_node.levels[0].forward
    return sorted_
