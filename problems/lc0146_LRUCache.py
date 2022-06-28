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
        self.__list_dummy_tail: LRUDoublyLinkedListNode = LRUDoublyLinkedListNode(key=0, val=0, prev=None, next=None)
        self.__list_dummy_head.next = self.__list_dummy_tail
        self.__list_dummy_tail.prev = self.__list_dummy_head

    def __len__(self) -> int:
        return len(self.__key_to_node)

    def __lookup_existing_node_and_update_list(self, key: int) -> LRUDoublyLinkedListNode | None:
        if key not in self.__key_to_node:
            return None
        node = self.__key_to_node[key]
        # 此时有效元素个数大于等于1
        if self.__list_dummy_head.next != node:  # 需要移动node
            self.__pop_existing_node_from_list(node)
            self.__insert_existing_node_at_front(node)
        return node

    def __pop_existing_node_from_list(self, node: LRUDoublyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        # 如果不写，那么仍然存在引用，垃圾永远不会被回收
        node.prev = None
        node.next = None

    def __insert_existing_node_at_front(self, node: LRUDoublyLinkedListNode) -> None:
        node.prev = self.__list_dummy_head
        node.next = self.__list_dummy_head.next
        self.__list_dummy_head.next.prev = node
        self.__list_dummy_head.next = node

    def get(self, key: int) -> int:
        node = self.__lookup_existing_node_and_update_list(key)
        return node.val if node is not None else -1

    def put(self, key: int, value: int) -> None:
        node = self.__lookup_existing_node_and_update_list(key)
        if node is not None:  # key in hash
            node.val = value
        else:  # key not in hash
            if len(self.__key_to_node) == self.__capacity:
                node_to_pop = self.__list_dummy_tail.prev
                self.__key_to_node.pop(node_to_pop.key)
                self.__pop_existing_node_from_list(node_to_pop)
            node: LRUDoublyLinkedListNode = LRUDoublyLinkedListNode(key=key, val=value, prev=None, next=None)
            self.__key_to_node[key] = node
            self.__insert_existing_node_at_front(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LFUDoublyLinkedListNode:
    def __init__(self, key, val, freq, prev=None, next=None):
        self.key: int = key
        self.val: int = val
        self.frequency: int = freq
        self.is_dummy_head: bool = False
        self.is_dummy_tail: bool = False
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
        self.__min_frequency: int | None = None
        self.__frequency_to_node_list: list[LFUDoublyLinkedListNode | None] = [None]  # (len == max_frequency + 1)

    def __max_frequency(self) -> int | None:
        return len(self.__frequency_to_node_list) - 1 if len(self.__key_to_node) > 0 else None

    def __len__(self) -> int:
        return len(self.__key_to_node)

    def __grow_frequency_list(self):
        list_dummy_head: LFUDoublyLinkedListNode = LFUDoublyLinkedListNode(key=0, val=0, freq=0, prev=None, next=None)
        list_dummy_head.is_dummy_head = True
        list_dummy_tail: LFUDoublyLinkedListNode = LFUDoublyLinkedListNode(key=0, val=0, freq=0, prev=None, next=None)
        list_dummy_tail.is_dummy_tail = True
        list_dummy_head.prev = list_dummy_tail

        list_dummy_head.next = list_dummy_tail
        list_dummy_tail.prev = list_dummy_head
        self.__frequency_to_node_list.append(list_dummy_head)

    def __lookup_existing_node_and_update_list(self, key: int) -> LFUDoublyLinkedListNode | None:
        if key not in self.__key_to_node:
            return None
        node = self.__key_to_node[key]
        # 此时有效元素个数大于等于1
        freq: int = node.frequency
        self.__pop_existing_node_from_list(node)
        if freq+1 > self.__max_frequency():
            self.__grow_frequency_list()
        self.__insert_existing_node_at_front(self.__frequency_to_node_list[freq+1], node)
        node.frequency += 1
        if freq == self.__min_frequency and self.__frequency_to_node_list[freq].next.is_dummy_tail:
            self.__min_frequency += 1
        return node

    def __pop_existing_node_from_list(self, node: LFUDoublyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        # 如果不写，那么仍然存在引用，垃圾永远不会被回收
        node.prev = None
        node.next = None

    def __insert_existing_node_at_front(self, dummy_head: LFUDoublyLinkedListNode, node: LFUDoublyLinkedListNode) -> None:
        node.prev = dummy_head
        node.next = dummy_head.next
        dummy_head.next.prev = node
        dummy_head.next = node

    def get(self, key: int) -> int:
        node = self.__lookup_existing_node_and_update_list(key)
        return node.val if node is not None else -1

    def put(self, key: int, value: int) -> None:
        node = self.__lookup_existing_node_and_update_list(key)
        if node is not None:  # key in hash
            node.val = value
        else:  # key not in hash
            if self.__capacity == 0:
                return
            if len(self.__key_to_node) == self.__capacity:
                node_to_pop = self.__frequency_to_node_list[self.__min_frequency].prev.prev
                self.__key_to_node.pop(node_to_pop.key)
                self.__pop_existing_node_from_list(node_to_pop)
                if len(self.__key_to_node) > 0:
                    while self.__frequency_to_node_list[self.__min_frequency].next.is_dummy_tail:
                        self.__min_frequency += 1
                else:
                    self.__min_frequency = None
                    self.__frequency_to_node_list = [None]

            freq: int = 1
            node: LFUDoublyLinkedListNode = LFUDoublyLinkedListNode(key=key, val=value, freq=freq, prev=None, next=None)

            if len(self.__key_to_node) == 0:
                self.__min_frequency = freq
                self.__grow_frequency_list()
            else:
                if freq < self.__min_frequency:
                    self.__min_frequency = freq
            self.__key_to_node[key] = node
            self.__insert_existing_node_at_front(self.__frequency_to_node_list[freq], node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
