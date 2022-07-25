from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if len(s) == 0 or len(words) == 0:
            raise "Invalid Input"

        word_len: int = len(words[0])
        window_size: int = len(words) * word_len

        # 最后一个有效的窗口第一个字符的索引i:
        # i + window_size - 1 <= len(s) - 1 可得 i <= len(s) - window_size

        window_first_char_idx_to_window: dict[int, list[str]] = \
            {i: Counter([
                s[word_start:word_start + word_len]
                for word_start
                in range(i, i + window_size, word_len)
            ])
                for i
                in range(0, len(s)-window_size+1)
            }

        result: list[int] = []
        target_window: Counter = Counter(words)
        for i, counter in window_first_char_idx_to_window.items():
            if all((counter[word] == target_window[word] for word in counter)):
                result.append(i)
        return result
