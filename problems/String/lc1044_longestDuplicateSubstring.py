from basics.data_structure.SuffixArray import SuffixArray


class Solution:

    # naive 的做法是把所有的子串都放到字典{substring: count}里，然后遍历出来

    def longestDupSubstring(self, s: str) -> str:
        suffix_array: SuffixArray = SuffixArray(s)

        from pprint import pprint
        pprint(suffix_array.suffix_array)
        pprint(suffix_array.suffix_start_index_array)
        pprint(suffix_array.longest_common_prefix_length_array)

        substrings: list[str] = []
        for i, suffix_start_index in enumerate(suffix_array.suffix_start_index_array):
            for j in range(1, len(suffix_array.suffix_array[i])+1):
                substrings.append(suffix_array.suffix_array[i][:j])
        print("substrings:")
        print(substrings)

        dup_substrings: list[str] = []
        for i, len_ in enumerate(suffix_array.longest_common_prefix_length_array):
            for j in range(1, len_+1):
                dup_substrings.append(suffix_array.suffix_array[i][:j])
        print("dup_substrings:")
        print(dup_substrings)

        max_len = -float("inf")
        max_len_dup_substring = ""
        for i, len_ in enumerate(suffix_array.longest_common_prefix_length_array):
            if len_ > max_len:
                max_len = len_
                max_len_dup_substring = suffix_array.suffix_array[i][:len_]

        return max_len_dup_substring


if __name__ == '__main__':
    print(Solution().longestDupSubstring("AZAZA"))
