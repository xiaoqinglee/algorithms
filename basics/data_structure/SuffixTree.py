from basics.data_structure.RadixTree import RadixTree


class SuffixTree:
    def __init__(self, word: str):
        self.radix_tree = RadixTree()
        for suffix_starting_index in range(len(word)-1, -1, -1):
            self.radix_tree.insert(word=word[suffix_starting_index:], word_attachment=suffix_starting_index)

    def ends_with(self, suffix: str) -> bool:
        found, suffix_starting_index = self.radix_tree.search(suffix)
        return found

    def is_substring(self, substring: str) -> bool:
        return self.radix_tree.starts_with(substring)

    def substring_matching_indexes(self, substring: str) -> list[int]:
        matching_indexes: list[int] = []

        def get_leaf_indexes(tree: RadixTree | None) -> None:
            if tree is None:
                return
            if tree.is_terminal():
                matching_indexes.append(tree.full_word_attachment)
                return
            for char in range(ord(tree.TERMINAL_CHAR), ord(tree.TERMINAL_CHAR) + 26 + 1):
                get_leaf_indexes(tree.children.get(chr(char), None))

        substring += self.radix_tree.TERMINAL_CHAR
        word_suffix = substring
        node = self.radix_tree

        while True:
            child: RadixTree | None = node.children.get(word_suffix[0], None)
            # assert node is an internal node, node might be the root
            if child is None:
                if word_suffix[0] == self.radix_tree.TERMINAL_CHAR and len(node.children) > 0:
                    get_leaf_indexes(node)
                    matching_indexes.sort()
                    return matching_indexes
                else:
                    return []

            common_prefix, string1_suffix, string2_suffix = \
                self.radix_tree.cut_strings_at_diverging_index(child.label, word_suffix)
            assert len(common_prefix) > 0
            if string1_suffix == string2_suffix == "":
                assert common_prefix[-1] == self.radix_tree.TERMINAL_CHAR
                return [child.full_word_attachment]
            elif string1_suffix == "" and string2_suffix != "":
                assert common_prefix[-1] != self.radix_tree.TERMINAL_CHAR
                word_suffix = string2_suffix
                node = child
            elif string1_suffix != "" and string2_suffix == "":  # 这种情况不存在
                pass
            else:  # string1_suffix != "" and string2_suffix != ""
                if string2_suffix[0] == self.radix_tree.TERMINAL_CHAR:
                    get_leaf_indexes(child)
                    matching_indexes.sort()
                    return matching_indexes
                else:
                    return []
