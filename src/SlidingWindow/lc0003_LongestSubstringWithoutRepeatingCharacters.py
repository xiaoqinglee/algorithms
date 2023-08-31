# https://leetcode.cn/problems/longest-substring-without-repeating-characters
def longest_substring_without_repeating_characters(s: str) -> int:
	index_start: int = 0  # 包含
	index_end: int = 0  # 包含
	length: int = 0
	maxlength: int = length
	substring_char_to_index_dict: dict[str, int] = {}
	for index, char in enumerate(s):
		repeating_char_index = substring_char_to_index_dict.get(char)
		if repeating_char_index is not None:
			for substring_index in range(index_start, repeating_char_index+1):
				# help(dict.pop)
				# Help on method_descriptor:
				#
				# pop(...)
				#     D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
				#
				#     If the key is not found, return the default if given; otherwise,
				#     raise a KeyError.
				# 此处不会出现key不存在的情况
				substring_char_to_index_dict.pop(s[substring_index])
			index_start = repeating_char_index + 1
		substring_char_to_index_dict[char] = index
		index_end = index
		length = index_end - index_start + 1
		maxlength = length if length > maxlength else maxlength
	return maxlength
