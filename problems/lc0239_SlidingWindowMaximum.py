import heapq


class Solution:
	def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
		results: list[int] = []
		negative_num_and_num_index_pairs: list[tuple[int, int]] = []
		# 窗口内最后一个元素的下标是right
		for right, num in enumerate(nums):
			# heapq被设计成最小堆
			heapq.heappush(negative_num_and_num_index_pairs, (-num, right))

			if right < k-1:
				continue
			if right == k-1:
				heapq.heapify(negative_num_and_num_index_pairs)

			while right - negative_num_and_num_index_pairs[0][1] >= k:
				heapq.heappop(negative_num_and_num_index_pairs)
			results.append(-negative_num_and_num_index_pairs[0][0])

		return results
