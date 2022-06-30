class Trie:
    ARRAY_LEN = 26

    def __init__(self):
        self.is_terminal: bool = False
        self.value: str | None = None  # 仅当self.is_terminal为True时有意义
        self.value_count: int = 0  # 仅当self.is_terminal为True时有意义
        self.children: list[Trie | None] = [None] * self.ARRAY_LEN
        self.child_count: int = 0

    def insert(self, word: str) -> None:
        node: Trie = self
        for char in word:
            node.child_count += 1
            child: Trie | None = node.children[ord(char) - ord('a')]
            if child is None:
                # print("inserting", char)
                child = Trie()
                node.children[ord(char) - ord('a')] = child
            node = child
        if node.is_terminal:
            node.value_count += 1
        else:
            node.is_terminal = True
            node.value = word
            node.value_count = 1

    def delete(self, word: str) -> None:
        parent_nodes_to_update: list[Trie] = []
        paths_leading_to_child_node: list[str] = []

        node: Trie = self
        for char in word:
            parent_nodes_to_update.append(node)
            paths_leading_to_child_node.append(char)
            child: Trie | None = node.children[ord(char) - ord('a')]
            if child is None:
                raise "word not in trie"
            node = child

        if not node.is_terminal:
            raise "word not in trie"
        if node.value_count > 1:
            node.value_count -= 1
        elif node.value_count == 1:
            node.is_terminal = False

        child_is_kept: bool | None = None
        if not node.is_terminal and node.child_count == 0:
            # print("deleting node", node.value)
            child_is_kept = False
        else:
            child_is_kept = True

        while len(parent_nodes_to_update) > 0:
            node: node = parent_nodes_to_update.pop()
            path_leading_to_child: str = paths_leading_to_child_node.pop()
            node.child_count -= 1

            if child_is_kept:
                continue
            # print("deleting path", path_leading_to_child)
            node.children[ord(path_leading_to_child)-ord('a')] = None

            if not node.is_terminal and node.child_count == 0:
                # print("deleting node", node.value)
                child_is_kept = False
            else:
                child_is_kept = True

    def search(self, word: str) -> bool:
        exists: bool = False
        node: Trie = self
        for char in word:
            node: Trie | None = node.children[ord(char) - ord('a')]
            if node is None:
                return exists
        if node.is_terminal:
            exists = True
            return exists
        return exists

    def startsWith(self, prefix: str) -> bool:
        exists: bool = False
        node: Trie = self
        for char in prefix:
            node: Trie | None = node.children[ord(char) - ord('a')]
            if node is None:
                return exists
        exists = node.is_terminal or node.child_count > 0
        return exists


# 叶子节点的数据为全null数组
# 叶子节点代表的字符串的最后一个字符是什么这个信息存在parent的children数组里面
# 一个空树只有一个root节点，self即是root
