class Solution:
    def longestWord(self, words: list[str]) -> str:

        # 找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。
        # 若有多个长度相同的结果，返回其中字典序最小的一项，
        # 若没有符合要求的单词则返回空字符串。

        def can_be_made_of(word: str, dictionary: dict[str, None]) -> bool:
            if word == "":
                return True
            else:
                return any((word[:idx] in dictionary and can_be_made_of(word[idx:], dictionary))
                           for idx in range(1, len(word)+1))

        words.sort(key=lambda word: (-len(word), word))
        for i in range(len(words)):
            # python 3.10 set 仍然不能保持元素添加的顺序, 所以使用dict
            if can_be_made_of(words[i], {word: None for word in (words[:i] + words[i+1:])}):
                return words[i]

        return ""
