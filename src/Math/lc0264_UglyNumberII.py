import heapq


# https://leetcode.cn/problems/ugly-number-ii
class Solution:
	def nthUglyNumber(self, n: int) -> int:
		pushed_ugly_numbers: set[int] = set()
		pushed_ugly_numbers.add(1)
		ugly_numbers: list[int] = [1]
		count = 0
		while True:
			min_ugly_number = heapq.heappop(ugly_numbers)
			count += 1
			if count == n:
				return min_ugly_number
			for i in [2, 3, 5]:
				new_ugly_number = min_ugly_number * i
				if new_ugly_number not in pushed_ugly_numbers:
					heapq.heappush(ugly_numbers, new_ugly_number)
					pushed_ugly_numbers.add(new_ugly_number)

