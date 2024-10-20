# https://leetcode.cn/problems/lru-cache
import collections


class LRUDoublyLinkedListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key: int = key
        self.val: int = val
        self.prev: LRUDoublyLinkedListNode = prev
        self.next: LRUDoublyLinkedListNode = next

    def __repr__(self):
        return repr({
            "prev_val": self.prev.val if self.prev is not None else None,
            "val": self.val,
            "next_val": self.next.val if self.next is not None else None
        })


class LRUCache:
    def __init__(self, capacity: int):
        if not capacity >= 1:
            raise "Invalid Input"
        self.__capacity = capacity
        self.__key_to_node: dict[int, LRUDoublyLinkedListNode] = {}
        dummy_node = LRUDoublyLinkedListNode(key=0, val=0, prev=None, next=None)
        self.__list_dummy_head: LRUDoublyLinkedListNode = dummy_node
        self.__list_dummy_tail: LRUDoublyLinkedListNode = dummy_node
        # dummy_node 同时作为 dummy_head 和 dummy_tail
        # dummy_node.next 指针给 dummy_head 身份使用, dummy_node.prev 指针给 dummy_tail 身份使用
        self.__list_dummy_head.next = self.__list_dummy_tail
        self.__list_dummy_tail.prev = self.__list_dummy_head

    def __len__(self) -> int:
        return len(self.__key_to_node)

    def __lookup_node_and_update_list(self, key: int) -> LRUDoublyLinkedListNode | None:
        if key not in self.__key_to_node:
            return None
        node = self.__key_to_node[key]
        # 此时有效元素个数大于等于1
        if self.__list_dummy_head.next != node:  # 需要移动node
            self.__pop_node_from_list(node)
            self.__insert_node_at_front(node)
        return node

    @staticmethod
    def __pop_node_from_list(node: LRUDoublyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        # 可以不写, node是否被gc取决于别人引用它的次数而不是它引用别人的次数.
        node.prev = None
        node.next = None

    def __insert_node_at_front(self, node: LRUDoublyLinkedListNode) -> None:
        node.prev = self.__list_dummy_head
        node.next = self.__list_dummy_head.next
        self.__list_dummy_head.next.prev = node
        self.__list_dummy_head.next = node

    def get(self, key: int) -> int:
        node = self.__lookup_node_and_update_list(key)
        return node.val if node is not None else -1

    def put(self, key: int, value: int) -> None:
        node = self.__lookup_node_and_update_list(key)
        if node is not None:  # key in hash
            node.val = value
        else:  # key not in hash
            if len(self.__key_to_node) == self.__capacity:  # assert self.__capacity >= 1
                node_to_pop = self.__list_dummy_tail.prev
                self.__key_to_node.pop(node_to_pop.key)
                self.__pop_node_from_list(node_to_pop)
            node: LRUDoublyLinkedListNode = LRUDoublyLinkedListNode(key=key, val=value, prev=None, next=None)
            self.__key_to_node[key] = node
            self.__insert_node_at_front(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# https://leetcode.cn/problems/lfu-cache
class LFUDoublyLinkedListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key: int = key
        self.val: int = val
        self.prev: LFUDoublyLinkedListNode = prev
        self.next: LFUDoublyLinkedListNode = next

    def __repr__(self):
        return repr({
            "prev_val": self.prev.val if self.prev is not None else None,
            "val": self.val,
            "next_val": self.next.val if self.next is not None else None
        })


class LFUCache:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__frequency_to_node_list: dict[int, LFUDoublyLinkedListNode] = \
            collections.defaultdict(self.__init_node_list)
        self.__key_to_node: dict[int, LFUDoublyLinkedListNode] = {}
        self.__key_to_frequency: dict[int, int] = {}
        self.__min_frequency: int = 0

    @staticmethod
    def __init_node_list() -> LFUDoublyLinkedListNode:
        dummy_node = LFUDoublyLinkedListNode(key=0, val=0, prev=None, next=None)
        list_dummy_head: LFUDoublyLinkedListNode = dummy_node
        list_dummy_tail: LFUDoublyLinkedListNode = dummy_node
        list_dummy_head.next = list_dummy_tail
        list_dummy_tail.prev = list_dummy_head
        return list_dummy_head

    def __len__(self) -> int:
        return len(self.__key_to_node)

    def __lookup_node_and_update_list(self, key: int) -> LFUDoublyLinkedListNode | None:
        if key not in self.__key_to_node:
            return None
        node = self.__key_to_node[key]
        freq: int = self.__key_to_frequency[key]
        self.__pop_node_from_list(node)
        self.__insert_node_at_front(self.__frequency_to_node_list[freq + 1], node)
        self.__key_to_frequency[key] = freq + 1
        assert self.__min_frequency <= freq
        if self.__min_frequency == freq and self.__node_list_is_empty(self.__frequency_to_node_list[freq]):
            self.__min_frequency = freq + 1
        return node

    @staticmethod
    def __pop_node_from_list(node: LFUDoublyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        # 可以不写, node是否被gc取决于别人引用它的次数而不是它引用别人的次数.
        node.prev = None
        node.next = None

    @staticmethod
    def __node_list_is_empty(dummy_head: LFUDoublyLinkedListNode) -> bool:
        return dummy_head.next == dummy_head and dummy_head.prev == dummy_head

    @staticmethod
    def __insert_node_at_front(dummy_head: LFUDoublyLinkedListNode, node: LFUDoublyLinkedListNode) -> None:
        node.prev = dummy_head
        node.next = dummy_head.next
        dummy_head.next.prev = node
        dummy_head.next = node

    def get(self, key: int) -> int:
        if self.__capacity == 0:
            return -1
        node = self.__lookup_node_and_update_list(key)
        return node.val if node is not None else -1

    def put(self, key: int, value: int) -> None:
        if self.__capacity == 0:
            return
        node = self.__lookup_node_and_update_list(key)
        if node is not None:  # key in hash
            node.val = value
        else:  # key not in hash and assert self.__capacity > 0
            if len(self.__key_to_node) == self.__capacity:
                node_to_pop = self.__frequency_to_node_list[self.__min_frequency].prev
                self.__pop_node_from_list(node_to_pop)
                self.__key_to_node.pop(node_to_pop.key)
                self.__key_to_frequency.pop(node_to_pop.key)

            freq: int = 1
            node: LFUDoublyLinkedListNode = LFUDoublyLinkedListNode(key=key, val=value, prev=None, next=None)
            self.__insert_node_at_front(self.__frequency_to_node_list[freq], node)
            self.__key_to_node[key] = node
            self.__key_to_frequency[key] = freq
            self.__min_frequency = freq

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
