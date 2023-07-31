import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        if h < len(piles): # 无论怎样都吃不完
            return -1

        def can_eat_up(speed: int) -> bool:
            need_hours = 0
            for count_in_one_pile in piles:
                need_hours += math.ceil(count_in_one_pile / speed)
            return need_hours <= h

        # 已知从左到右遍历 array[lo, hi], 从某个 index 开始, 后续 index 上的元素均满足条件.
        # array[hi] 满足条件.
        # 返回 array[lo, hi] 内第一个满足条件的元素的 index.

        # 等价表述:

        # 已知从左到右遍历 array[lo, hi), 从某个 index 开始, 后续 index 上的元素均满足条件.
        # 返回 array[lo, hi) 内第一个满足条件的元素的 index, 如果找不到, 返回 hi.

        def search_min_speed(lo: int, hi: int) -> int:
            while True:
                if lo == hi:
                    return lo
                mid = (lo + hi) // 2
                if can_eat_up(mid):
                    hi = mid
                else:
                    lo = mid + 1

        return search_min_speed(1, max(piles))
