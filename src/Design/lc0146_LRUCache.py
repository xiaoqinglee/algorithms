# https://leetcode.cn/problems/lru-cache
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
        self.__list_dummy_head: LRUDoublyLinkedListNode = LRUDoublyLinkedListNode(key=0, val=0, prev=None, next=None)
        self.__list_dummy_tail: LRUDoublyLinkedListNode = self.__list_dummy_head
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
    def __init__(self, key, val, freq, prev=None, next=None):
        self.key: int = key
        self.val: int = val
        self.frequency: int = freq
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
        self.__key_to_node: dict[int, LFUDoublyLinkedListNode] = {}
        self.__frequency_to_node_list: dict[int, LFUDoublyLinkedListNode] = {}  # key从1开始

    def __min_frequency(self) -> int:  # 没有元素的时候返回值等于0, 有元素的时候返回值大于等于1
        if len(self.__key_to_node) == 0:
            return 0
        for freq in range(1, len(self.__frequency_to_node_list) + 1):
            if self.__frequency_to_node_list[freq].next != self.__frequency_to_node_list[freq]:
                return freq

    def __init_node_list_for_specific_frequency(self, freq: int) -> None:
        list_dummy_head: LFUDoublyLinkedListNode \
            = LFUDoublyLinkedListNode(key=0, val=0, freq=freq, prev=None, next=None)
        list_dummy_tail = list_dummy_head
        list_dummy_head.next = list_dummy_tail
        list_dummy_tail.prev = list_dummy_head
        self.__frequency_to_node_list[freq] = list_dummy_head

    def __len__(self) -> int:
        return len(self.__key_to_node)

    def __lookup_node_and_update_list(self, key: int) -> LFUDoublyLinkedListNode | None:
        if key not in self.__key_to_node:
            return None
        node = self.__key_to_node[key]
        # 此时有效元素个数大于等于1
        freq: int = node.frequency
        self.__pop_node_from_list(node)
        if freq+1 not in self.__frequency_to_node_list:
            self.__init_node_list_for_specific_frequency(freq + 1)
        self.__insert_node_at_front(self.__frequency_to_node_list[freq + 1], node)
        node.frequency = freq + 1
        return node

    @staticmethod
    def __pop_node_from_list(node: LFUDoublyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        # 可以不写, node是否被gc取决于别人引用它的次数而不是它引用别人的次数.
        node.prev = None
        node.next = None

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
                node_to_pop = self.__frequency_to_node_list[self.__min_frequency()].prev
                self.__pop_node_from_list(node_to_pop)
                self.__key_to_node.pop(node_to_pop.key)

            freq: int = 1
            node: LFUDoublyLinkedListNode = LFUDoublyLinkedListNode(key=key, val=value, freq=freq, prev=None, next=None)
            if freq not in self.__frequency_to_node_list:
                self.__init_node_list_for_specific_frequency(freq)
            self.__insert_node_at_front(self.__frequency_to_node_list[freq], node)
            self.__key_to_node[key] = node


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
