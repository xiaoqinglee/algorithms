# Definition for singly-linked list.
import collections.abc


class ListNode:
    def __init__(self, val, next=None):
        self.val: int = val
        self.next: ListNode = next


class DoubleLinkedListNode:
    def __init__(self, val, prev=None, next=None):
        self.val: int = val
        self.prev: DoubleLinkedListNode = prev
        self.next: DoubleLinkedListNode = next


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class PriorityQueue:
    def __init__(self,
                 elements: list[int],
                 has_higher_priority: collections.abc.Callable[[int, int], bool]):
        self.__elements = elements.copy()
        self.__has_higher_priority = has_higher_priority
        self.__heapify()

    def __heapify(self) -> None:
        for element_index in range(self.size() - 1, -1, -1):
            self.__sink_down(element_index)

    def __swim_up(self, element_index: int) -> None:
        while True:
            if element_index == 0:
                break
            index_of_parent = (element_index - 1) // 2
            if self.__has_higher_priority(self.__elements[index_of_parent], self.__elements[element_index]):
                break
            self.__elements[element_index], self.__elements[index_of_parent] = \
                self.__elements[index_of_parent], self.__elements[element_index]
            element_index = index_of_parent

    def __sink_down(self, element_index: int) -> None:
        while True:
            children_indexes = []
            if 2*element_index + 1 <= self.size() - 1:
                children_indexes.append(2*element_index + 1)
            if 2*element_index + 2 <= self.size() - 1:
                children_indexes.append(2*element_index + 2)
            if len(children_indexes) == 0:
                break
            if len(children_indexes) == 1:
                index_of_child_with_higher_priority = children_indexes[0]
            elif len(children_indexes) == 2:
                index_of_child_with_higher_priority = children_indexes[0] \
                    if self.__has_higher_priority(self.__elements[children_indexes[0]],
                                                  self.__elements[children_indexes[1]]) \
                    else children_indexes[1]
            if self.__has_higher_priority(self.__elements[element_index],
                                          self.__elements[index_of_child_with_higher_priority]):
                break
            self.__elements[index_of_child_with_higher_priority], self.__elements[element_index] = \
                self.__elements[element_index], self.__elements[index_of_child_with_higher_priority]
            element_index = index_of_child_with_higher_priority

    def size(self) -> int:
        return len(self.__elements)

    def is_empty(self) -> bool:
        return self.size() == 0

    def top(self) -> int:
        if self.is_empty():
            raise "Empty heap"
        return self.__elements[0]

    def pop(self) -> int:
        top = self.top()
        self.__elements[0] = self.__elements[self.size() - 1]
        self.__elements = self.__elements[:-1]
        self.__sink_down(0)
        return top

    def insert(self, element: int) -> None:
        self.__elements.append(element)
        self.__swim_up(self.size() - 1)


# 叶子节点的数据为全null数组
# 叶子节点代表的字符串的最后一个字符是什么这个信息存在parent的children数组里面
# 一个空树只有一个root节点，self即是root
class Trie:
    ARRAY_LEN = 26

    def __init__(self):
        self.is_terminal: bool = False
        self.value: str | None = None
        self.value_count: int = 0
        self.children: list[Trie | None] = [None] * self.ARRAY_LEN

    def insert(self, word: str) -> None:
        node: Trie = self
        for char in word:
            child: Trie | None = node.children[ord(char) - ord('a')]
            if child is None:
                print("inserting", char)
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
        nodes_to_delete: list[Trie] = []
        paths_to_delete: list[str] = []

        node: Trie = self
        for char in word:
            child: Trie | None = node.children[ord(char) - ord('a')]
            if child is None:
                raise "word not in trie"
            node = child
            nodes_to_delete.append(node)
            paths_to_delete.append(char)

        if not node.is_terminal:
            raise "word not in trie"
        if node.value_count > 1:
            node.value_count -= 1
        elif node.value_count == 1:
            node.is_terminal = False

        child_is_kept: bool | None = None
        if not node.is_terminal and all(x is None for x in node.children):
            print("deleting node", node.value)
            child_is_kept = False
        else:
            child_is_kept = True

        nodes_to_delete.pop()
        path_leading_to_child: str = paths_to_delete.pop()

        while len(nodes_to_delete) > 0:
            node = nodes_to_delete.pop()
            if child_is_kept:
                return
            print("deleting path", path_leading_to_child)
            node.children[ord(path_leading_to_child)-ord('a')] = None

            if not node.is_terminal and all(x is None for x in node.children):
                print("deleting node", node.value)
                child_is_kept = False
            else:
                child_is_kept = True
            path_leading_to_child = paths_to_delete.pop()

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
        exists = True
        return exists


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    obj = Trie()
    print("=============================")
    print('''obj.insert("leetcode")''')
    obj.insert("leetcode")
    print('''obj.insert("leef")''')
    obj.insert("leef")
    print('''obj.insert("leet")''')
    obj.insert("leet")
    print('''obj.search("leetcode")''')
    print(obj.search("leetcode"))
    print('''obj.search("leef")''')
    print(obj.search("leet"))
    print('''obj.search("leet")''')
    print(obj.search("leef"))

    print("=============================")
    print('''obj.delete("leetcode")''')
    obj.delete("leetcode")
    print('''obj.delete("leet")''')
    obj.delete("leet")

    print("=============================")
    print('''obj.search("leetcode")''')
    print(obj.search("leetcode"))
    print('''obj.search("leef")''')
    print(obj.search("leet"))
    print('''obj.search("leet")''')
    print(obj.search("leef"))

    print('''obj.startsWith("l")''')
    print(obj.startsWith("l"))
    print('''obj.startsWith("")''')
    print(obj.startsWith(""))
    print('''obj.search("")''')
    print(obj.search(""))
