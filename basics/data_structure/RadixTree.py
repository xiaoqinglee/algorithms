from typing import Any


Char = str


class RadixTree:
    TERMINAL_CHAR = chr(ord("a") - 1)

    @staticmethod
    def cut_strings_at_diverging_index(string1: str, string2: str) -> tuple[str, str, str]:
        # return tuple[common_prefix, string1_suffix, string2_suffix]
        index = 0
        index_max = min(len(string1), len(string2)) - 1
        while index <= index_max and string1[index] == string2[index]:
            index += 1
        return string1[0: index], string1[index:], string2[index:]

    def __init__(self, label: str = ""):
        # 我们要求 root 节点的 label 永远为空串, 所以当树中只有一个word的时候, 树有两个 node
        self.label = label  # path leading to this node
        self.full_word: str | None = None  # 仅当是叶子节点时有意义
        self.full_word_count: int = 0  # 仅当是叶子节点时有意义
        self.full_word_attachment: Any = None  # 仅当是叶子节点时有意义
        self.children: dict[Char, RadixTree] = {}  # maps characters to nodes

    def is_terminal(self) -> int:
        # if self is terminal, assert len(self.children) == 0 and self is not the root
        return len(self.label) > 0 and self.label[-1] == self.TERMINAL_CHAR

    def insert(self, word: str, word_attachment: Any = None) -> None:
        word += self.TERMINAL_CHAR
        word_suffix = word
        node = self
        while True:
            child: RadixTree | None = node.children.get(word_suffix[0], None)
            if child is None:
                new_leaf: RadixTree = RadixTree(label=word_suffix)
                new_leaf.full_word = word[:-1]
                new_leaf.full_word_count = 1
                new_leaf.full_word_attachment = word_attachment
                node.children[word_suffix[0]] = new_leaf
                return
            common_prefix, string1_suffix, string2_suffix = \
                self.cut_strings_at_diverging_index(child.label, word_suffix)
            assert len(common_prefix) > 0
            if string1_suffix == string2_suffix == "":
                assert common_prefix[-1] == self.TERMINAL_CHAR
                child.full_word_count += 1
                child.full_word_attachment = word_attachment
                return
            elif string1_suffix == "" and string2_suffix != "":
                assert common_prefix[-1] != self.TERMINAL_CHAR
                word_suffix = string2_suffix
                node = child
            elif string1_suffix != "" and string2_suffix == "":  # 这种情况不存在
                pass
            else:  # string1_suffix != "" and string2_suffix != ""

                new_internal_node: RadixTree = RadixTree(label=common_prefix)

                child.label = string1_suffix

                new_leaf: RadixTree = RadixTree(label=string2_suffix)
                new_leaf.full_word = word[:-1]
                new_leaf.full_word_count = 1
                new_leaf.full_word_attachment = word_attachment

                new_internal_node.children[string1_suffix[0]] = child
                new_internal_node.children[string2_suffix[0]] = new_leaf

                node.children[common_prefix[0]] = new_internal_node

                return

    def delete(self, word: str) -> None:
        word += self.TERMINAL_CHAR
        word_suffix = word
        node = self

        parent_nodes_to_update: list[RadixTree] = []  # root 在这个栈里， 但是 root node 永远不会被 delete
        paths_leading_to_child_node: list[str] = []

        while True:
            child: RadixTree | None = node.children.get(word_suffix[0], None)
            if child is None:
                raise "word not exists"

            parent_nodes_to_update.append(node)
            paths_leading_to_child_node.append(child.label)

            common_prefix, string1_suffix, string2_suffix = \
                self.cut_strings_at_diverging_index(child.label, word_suffix)
            assert len(common_prefix) > 0
            if string1_suffix == string2_suffix == "":
                assert common_prefix[-1] == self.TERMINAL_CHAR
                if child.full_word_count == 1:
                    leaf_is_kept = False
                else:
                    leaf_is_kept = True
                    child.full_word_count -= 1
                break
            elif string1_suffix == "" and string2_suffix != "":
                assert common_prefix[-1] != self.TERMINAL_CHAR
                word_suffix = string2_suffix
                node = child
            elif string1_suffix != "" and string2_suffix == "":  # 这种情况不存在
                pass
            else:  # string1_suffix != "" and string2_suffix != ""
                raise "word not exists"

        if not leaf_is_kept:
            node: RadixTree = parent_nodes_to_update.pop()
            path_leading_to_child: str = paths_leading_to_child_node.pop()

            # print("deleting path", path_leading_to_child)
            del node.children[path_leading_to_child[0]]  # 一个path只指向一个node

            if len(node.children) == 1 and len(parent_nodes_to_update) > 0:
                # 压缩
                # leaf node len(root.children) == 0
                # internal node 中只有 root node len(root.children) 可以等于[0, 26+1]
                # 其他 internal node len(root.children) 等于 [2, 26+1]
                (char, grand_child) = node.children.popitem()
                parent: RadixTree = parent_nodes_to_update.pop()
                grand_child.label = node.label + grand_child.label
                parent.children[node.label[0]] = grand_child

    def search(self, word: str) -> tuple[bool, Any]:
        # return tuple[found_or_note, word_attachment]
        word += self.TERMINAL_CHAR
        word_suffix = word
        node = self

        while True:
            child: RadixTree | None = node.children.get(word_suffix[0], None)
            if child is None:
                return False, None

            common_prefix, string1_suffix, string2_suffix = \
                self.cut_strings_at_diverging_index(child.label, word_suffix)
            assert len(common_prefix) > 0
            if string1_suffix == string2_suffix == "":
                assert common_prefix[-1] == self.TERMINAL_CHAR
                return True, child.full_word_attachment
            elif string1_suffix == "" and string2_suffix != "":
                assert common_prefix[-1] != self.TERMINAL_CHAR
                word_suffix = string2_suffix
                node = child
            elif string1_suffix != "" and string2_suffix == "":  # 这种情况不存在
                pass
            else:  # string1_suffix != "" and string2_suffix != ""
                return False, None

    def starts_with(self, prefix: str) -> bool:
        word_suffix = prefix
        node = self

        if word_suffix == "":
            return len(node.children) > 0  # node is the root

        while True:
            child: RadixTree | None = node.children.get(word_suffix[0], None)
            if child is None:
                return False

            common_prefix, string1_suffix, string2_suffix = \
                self.cut_strings_at_diverging_index(child.label, word_suffix)
            assert len(common_prefix) > 0

            if string1_suffix == string2_suffix == "":
                # assert child is an internal node, child can not be the root
                return True
            elif string1_suffix == "" and string2_suffix != "":
                word_suffix = string2_suffix
                node = child
            elif string1_suffix != "" and string2_suffix == "":
                return True
            else:  # string1_suffix != "" and string2_suffix != ""
                return False


# https://www.cs.jhu.edu/~langmea/resources/lecture_notes/suffix_trees.pdf
# https://nbviewer.org/gist/BenLangmead/6665861


if __name__ == "__main__":
    t = RadixTree()
    print("======")
    t.insert("hello")
    print(t.search(""))
    print(t.starts_with(""))
    print("==============")
    t.insert("")
    print(t.search(""))
    print(t.starts_with(""))
    print("============================")
    t.delete("")
    print(t.search(""))
    print(t.starts_with(""))
    print("======")
    t.delete("hello")
    print(t.search(""))
    print(t.starts_with(""))
    print("================")
