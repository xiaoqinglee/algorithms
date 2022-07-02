import pprint
from basics.data_structure.SuffixTree import SuffixTree


class Suffix:
    def __init__(self, suffix: str, suffix_start_index: int):
        self.suffix = suffix
        self.suffix_start_index = suffix_start_index
        self.longest_common_prefix_length = 0


class SuffixArray:

    @staticmethod
    def compute_longest_common_prefix_length(string1: str, string2: str) -> int:
        index = 0
        index_max = min(len(string1), len(string2)) - 1
        while index <= index_max and string1[index] == string2[index]:
            index += 1
        return index

    def __init__(self, word: str):
        self.suffix_array: list[str] = []
        self.suffix_start_index_array: list[int] = []
        self.longest_common_prefix_length_array: list[int] = []

        suffixes: list[Suffix] = [Suffix(word[left:], left) for left in range(len(word)+1)]  # 包含末尾的空串后缀
        suffixes.sort(key=lambda suffix_class_instance: suffix_class_instance.suffix)
        for i, suffix_instance in enumerate(suffixes):
            self.suffix_array.append(suffix_instance.suffix)
            self.suffix_start_index_array.append(suffix_instance.suffix_start_index)
            lcp_len = (0
                       if i == 0
                       else self.compute_longest_common_prefix_length(self.suffix_array[i-1], self.suffix_array[i]))
            suffix_instance.longest_common_prefix_length = lcp_len
            self.longest_common_prefix_length_array.append(lcp_len)

    def __repr__(self):
        return pprint.pformat([
            self.suffix_array,
            self.suffix_start_index_array,
            self.longest_common_prefix_length_array
        ])

    def ends_with(self, suffix: str) -> bool:

        def binary_search(lo: int, hi: int) -> bool:
            while True:
                if lo > hi:
                    return False
                mid = (lo + hi) // 2
                if self.suffix_array[mid] < suffix:
                    lo = mid + 1
                elif self.suffix_array[mid] > suffix:
                    hi = mid - 1
                else:
                    return True

        return binary_search(0, len(self.suffix_array) - 1)

    def is_substring(self, substring: str) -> bool:
        return len(self.substrings(substring)) > 0

    def substrings(self, substring: str) -> list[int]:

        # 两次二分查找, 目标区间是 [lower, upper)

        # lower_boundary是第一个满足suffix[:len(substring)] >= substring的元素的索引
        def binary_search_lower_boundary(lo: int, hi: int) -> int:
            # 返回值范围[0...len()]: 所有元素都满足 -> 0, 所有元素都不满足 -> len()
            while True:
                if lo == hi:
                    return lo
                mid = (lo + hi) // 2
                if self.suffix_array[mid][:len(substring)] < substring:
                    lo = mid + 1
                else:  # self.suffix_array[mid][:len(substring)] >= substring
                    hi = mid

        # upper_boundary是第一个满足suffix[:len(substring)] > substring的元素的索引
        def binary_search_upper_boundary(lo: int, hi: int) -> int:
            # 返回值范围[0...len()]: 所有元素都满足 -> 0, 所有元素都不满足 -> len()
            while True:
                if lo == hi:
                    return lo
                mid = (lo + hi) // 2
                if self.suffix_array[mid][:len(substring)] <= substring:
                    lo = mid + 1
                else:  # self.suffix_array[mid][:len(substring)] > substring
                    hi = mid

        lower_boundary = binary_search_lower_boundary(0, len(self.suffix_array))
        upper_boundary = binary_search_upper_boundary(0, len(self.suffix_array))

        return sorted(self.suffix_start_index_array[lower_boundary: upper_boundary])


if __name__ == '__main__':

    suffix_array = SuffixArray("mississippi")
    print(repr(suffix_array))

    print(suffix_array.substrings("a"))
    print(suffix_array.substrings("z"))
    print(suffix_array.substrings("ssq"))

    print(suffix_array.substrings("m"))
    print(suffix_array.substrings("i"))

    print(suffix_array.substrings("ssi"))
    print(suffix_array.substrings("si"))

    print(suffix_array.ends_with("sippi"))
    print(suffix_array.ends_with("pp"))
    print(suffix_array.ends_with(""))

    suffix_tree = SuffixTree("mississippi")

    print(suffix_tree.substrings("a"))
    print(suffix_tree.substrings("z"))
    print(suffix_tree.substrings("ssq"))

    print(suffix_tree.substrings("m"))
    print(suffix_tree.substrings("i"))

    print(suffix_tree.substrings("ssi"))
    print(suffix_tree.substrings("si"))

    print(suffix_tree.ends_with("sippi"))
    print(suffix_tree.ends_with("pp"))
    print(suffix_tree.ends_with(""))
