# 一. 整数排序
# 1. LSD（Least significant digital）：排序方式由数值的最右边（低位）开始
def radix_sort_lsd(nums: list[int]) -> list[int]:
    if len(nums) == 0:
        return nums

    num_strings: list[str] = [str(num) for num in nums]
    digit_count = max(len(num_string) for num_string in num_strings)

    def get_lowest_nth_digit(string: str, nth: int) -> str:
        if len(string) - nth < 0:
            return '0'
        return string[-nth]

    bucket_keys = "0123456789"
    buckets: dict[str, list[str]] = {key: [] for key in bucket_keys}

    for nth_digit in range(1, digit_count + 1):
        for num_string in num_strings:
            buckets[get_lowest_nth_digit(num_string, nth_digit)].append(num_string)
        num_strings = []
        for key in bucket_keys:
            num_strings.extend(buckets[key])
            buckets[key] = []

    return [int(num_string) for num_string in num_strings]


# 2. MSD（Most significant digital）：由数值的最左边（高位）开始。
# 2.(1) 使用递归
def radix_sort_msd(nums: list[int]) -> list[int]:
    if len(nums) == 0:
        return nums

    num_strings: list[str] = [str(num) for num in nums]
    digit_count = max(len(num_string) for num_string in num_strings)

    def get_lowest_nth_digit(string: str, nth: int) -> str:
        if len(string) - nth < 0:
            return '0'
        return string[-nth]

    def get_highest_nth_digit(string: str, nth: int) -> str:
        return get_lowest_nth_digit(string, digit_count + 1 - nth)

    bucket_keys = "0123456789"

    def sort(sorted_n_digits: int, strings: list[str]) -> list[str]:
        if sorted_n_digits == digit_count:
            return strings
        buckets: dict[str, list[str]] = {key: [] for key in bucket_keys}
        for num_string in strings:
            buckets[get_highest_nth_digit(num_string, sorted_n_digits + 1)].append(num_string)
        strings = []
        for key in bucket_keys:
            strings.extend(sort(sorted_n_digits + 1, buckets[key]))
        return strings

    num_strings = sort(0, num_strings)
    return [int(num_string) for num_string in num_strings]


# 2.(2) 使用Trie树
# 将数字整形成等长字符串，从高位向低位构建单词，将单词逐一插入Trie树中，略。

# 二. 单词排序 (符合 MSD 情景，使用Trie树, 排序结果即是先序遍历结果)
def radix_sort_msd_using_trie(words: list[str]) -> list[str]:
    from pypkg.datatype import Trie
    trie: Trie = Trie()
    for word in words:
        trie.insert(word)

    sorted_words: list[str] = []

    def traverse(trie: Trie | None) -> None:
        if trie is None:
            return
        if trie.is_terminal:
            for n_times in range(trie.value_count):
                sorted_words.append(trie.value)
        for child in trie.children:
            traverse(child)

    traverse(trie)
    return sorted_words


if __name__ == '__main__':
    print(radix_sort_lsd([1, 124, 35, 4]))
    print(radix_sort_msd([1, 124, 35, 4]))
    print(radix_sort_msd_using_trie(["leef", "leetcode", "leef", "leet", "michael", "leave", "alike"]))
