Char = str


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        croak: str = "croak"

        n_frogs_min: int | float = -float("inf")

        # key: last char of prefix
        # count: prefix count
        prefix_to_prefix_count: dict[Char, int] = {k: 0 for k in croak}

        char_to_prev_char: dict[Char, Char] = {croak[i]: croak[i-1] for i in range(1, len(croak))}

        # 没有字符交错的两个"croak"叫声可以来自同一个青蛙
        # 有字符交错的两个"croak"叫声肯定来自两个青蛙
        for char in croakOfFrogs:
            if char == croak[0]:
                prefix_to_prefix_count[char] += 1
            else:
                prefix_to_prefix_count[char_to_prev_char[char]] -= 1
                if prefix_to_prefix_count[char_to_prev_char[char]] < 0:
                    return -1
                prefix_to_prefix_count[char] += 1
            if char == croak[-1]:
                # 青蛙的最小个数是所有叫声交错的事件中, 参与蛙最多的那一次事件的参与蛙数
                n_frogs_min = max(n_frogs_min, sum([count for prefix, count in prefix_to_prefix_count.items()]))
                prefix_to_prefix_count[croak[-1]] = 0

        # 最终残留了半个croak 或 残留了许多半个croak
        if sum([v for k, v in prefix_to_prefix_count.items()]) > 0:
            return -1
        return n_frogs_min
