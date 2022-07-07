def binary_search(nums: list[int], target: int) -> int:
	if len(nums) == 0:
		return -1
	left_index = 0
	right_index = len(nums) - 1
	while True:
		if left_index > right_index:
			return - 1
		mid_index = (left_index + right_index) // 2
		if nums[mid_index] == target:
			return mid_index
		elif nums[mid_index] > target:
			right_index = mid_index - 1
		else:  # nums[mid_index] < target
			left_index = mid_index + 1
