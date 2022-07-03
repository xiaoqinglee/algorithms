import random


class Solution:

    def __init__(self, nums: list[int]):
        self.__original = nums.copy()
        self.__nums = nums.copy()

    def reset(self) -> list[int]:
        self.__nums = self.__original.copy()
        return self.__nums

    def shuffle(self) -> list[int]:
        self.__shuffle2()
        return self.__nums

    # # Return random integer in range [a, b], including both end points
    # random.randint(a, b)

    def __shuffle1(self) -> None:  # 给定元素序列，按序遍历序列逐步构建新列表，保持目标列表时刻乱序
        for index, _ in enumerate(self.__nums):
            random_slot = random.randint(0, index)
            if random_slot == index:
                continue
            self.__nums[random_slot], self.__nums[index] = self.__nums[index], self.__nums[random_slot]

    def __shuffle2(self) -> None:  # 模拟发牌，每次拿到的元素都是等可能的
        remaining_n_elements = len(self.__nums)
        while remaining_n_elements > 0:
            random_slot = random.randint(0, remaining_n_elements - 1)
            if random_slot != remaining_n_elements-1:
                self.__nums[random_slot], self.__nums[remaining_n_elements-1] =\
                    self.__nums[remaining_n_elements-1], self.__nums[random_slot]
            remaining_n_elements -= 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
