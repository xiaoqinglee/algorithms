def heap_sort(nums: list[int]) -> list[int]:
    # # 应对 leetcode极端测试用例: 升序超大数组
    # import random
    # random.shuffle(nums)

    if len(nums) == 0:
        return nums

    sorted_ = []
    from basics.data_structure.PriorityQueue import PriorityQueue
    heap = PriorityQueue(elements=nums, has_higher_priority=lambda x, y: x < y)  # 最小堆
    while not heap.is_empty():
        sorted_.append(heap.pop())

    sorted_2 = []
    heap = PriorityQueue(elements=[], has_higher_priority=lambda x, y: x < y)  # 最小堆
    for elem in nums:
        heap.insert(elem)
    while not heap.is_empty():
        sorted_2.append(heap.pop())

    return sorted_
