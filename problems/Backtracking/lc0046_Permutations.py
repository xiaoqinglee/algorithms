def permute(nums: list[int]) -> list[list[int]]:
	result: list[list[int]] = []

	def swap_two_elements_by_index(list_: list[int], i: int, j: int) -> None:
		list_[i], list_[j] = list_[j], list_[i]

	def back_trace(fixed_first_n_elements: int) -> None:
		if fixed_first_n_elements == len(nums):
			result.append(nums.copy())
			return
		for unfixed_element_index in range(fixed_first_n_elements, len(nums)):
			swap_two_elements_by_index(nums, fixed_first_n_elements, unfixed_element_index)
			back_trace(fixed_first_n_elements + 1)
			swap_two_elements_by_index(nums, unfixed_element_index, fixed_first_n_elements)

	back_trace(0)
	return result
