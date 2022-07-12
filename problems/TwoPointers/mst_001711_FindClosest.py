class Solution:
    def findClosest(self, words: list[str], word1: str, word2: str) -> int:
        word_to_indexes: dict[str, list[int]] = {}
        for i, word in enumerate(words):
            word_to_indexes.setdefault(word, []).append(i)

        if (word1 not in word_to_indexes) or (word2 not in word_to_indexes):
            raise "Invalid Input"

        min_distance: int | float = float("inf")
        word1_indexes = word_to_indexes[word1]
        word2_indexes = word_to_indexes[word2]
        # i in [0...len(word1_indexes)-1]
        # j in [0...len(word2_indexes)-1]
        i = j = 0
        while i <= len(word1_indexes)-1 and j <= len(word2_indexes)-1:
            if word1_indexes[i] < word2_indexes[j]:
                distance = word2_indexes[j] - word1_indexes[i]
                i += 1
            else:  # word1_indexes[i] > word2_indexes[j]
                distance = word1_indexes[i] - word2_indexes[j]
                j += 1
            min_distance = min(min_distance, distance)

        return min_distance
