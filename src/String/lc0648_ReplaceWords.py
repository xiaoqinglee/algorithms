# https://leetcode.cn/problems/replace-words
class Solution:

    # 如果继承词有许多可以形成它的词根，则用最短的词根替换它

    def replaceWords(self, dictionary: list[str], sentence: str) -> str: # 使用
        # 使用哈希表
        entries: set[str] = set(dictionary)
        words: list[str] = sentence.split()
        new_words: list[str] = words.copy()
        for word_index, word in enumerate(words):
            for i in range(len(word)):
                if word[:i+1] in entries:
                    new_words[word_index] = word[:i+1]
                    break

        return " ".join(new_words)

    def replaceWords2(self, dictionary: list[str], sentence: str) -> str: # 使用
        # 使用Trie
        from basics.data_structure.Trie import SimpleTrie
        entries = SimpleTrie()
        for entry in dictionary:
            entries.insert(entry)
        words: list[str] = sentence.split()
        new_words: list[str] = words.copy()
        for word_index, word in enumerate(words):
            for i in range(len(word)):
                if entries.search(word[:i+1]):
                    new_words[word_index] = word[:i+1]
                    break

        return " ".join(new_words)

