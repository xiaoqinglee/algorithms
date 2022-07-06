from basics.data_structure.RadixTree import RadixTree


class SuffixTree:
    def __init__(self, word: str):
        self.radix_tree = RadixTree()
        for suffix_starting_index in range(len(word), -1, -1):  # 包含末尾的空串后缀
            self.radix_tree.insert(word=word[suffix_starting_index:], word_attachment=suffix_starting_index)

    def ends_with(self, suffix: str) -> bool:
        found, suffix_starting_index = self.radix_tree.search(suffix)
        return found

    def is_substring(self, substring: str) -> bool:
        return self.radix_tree.starts_with(substring)

    def substrings(self, substring: str) -> list[int]:

        def get_leaf_indexes(tree: RadixTree | None) -> list[int]:

            substring_left_indexes: list[int] = []

            def _get_leaf_indexes(tree: RadixTree | None) -> None:
                if tree is None:
                    return
                if tree.is_terminal():
                    substring_left_indexes.append(tree.full_word_attachment)
                    return
                for char in range(ord(tree.TERMINAL_CHAR), ord(tree.TERMINAL_CHAR) + 26 + 1):
                    _get_leaf_indexes(tree.children.get(chr(char), None))

            _get_leaf_indexes(tree)
            return sorted(substring_left_indexes)

        word_suffix = substring
        node = self.radix_tree

        if word_suffix == "":
            return get_leaf_indexes(node)  # node is the root

        while True:
            child: RadixTree | None = node.children.get(word_suffix[0], None)
            if child is None:
                return []

            common_prefix, string1_suffix, string2_suffix = \
                self.radix_tree.cut_strings_at_diverging_index(child.label, word_suffix)
            assert len(common_prefix) > 0

            if string1_suffix == string2_suffix == "":
                # assert child is an internal node, child can not be the root
                return get_leaf_indexes(child)
            elif string1_suffix == "" and string2_suffix != "":
                word_suffix = string2_suffix
                node = child
            elif string1_suffix != "" and string2_suffix == "":
                return get_leaf_indexes(child)
            else:  # string1_suffix != "" and string2_suffix != ""
                return []


# https://www.youtube.com/watch?v=VA9m_l6LpwI
# https://www.youtube.com/watch?v=UrmjCSM7wDw
