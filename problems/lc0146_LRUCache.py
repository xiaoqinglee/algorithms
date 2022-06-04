class DoubleLinkedListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key: int = key
        self.val: int = val
        self.prev: DoubleLinkedListNode = prev
        self.next: DoubleLinkedListNode = next

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
        self.__hash: dict[int, DoubleLinkedListNode] = {}
        self.__list_dummy_head: DoubleLinkedListNode = DoubleLinkedListNode(key=0, val=0, prev=None, next=None)
        self.__list_dummy_tail: DoubleLinkedListNode = DoubleLinkedListNode(key=0, val=0, prev=None, next=None)
        self.__list_dummy_head.next = self.__list_dummy_tail
        self.__list_dummy_tail.prev = self.__list_dummy_head

    def __len__(self) -> int:
        return len(self.__hash)

    def __lookup_existing_node_and_update_list(self, key: int) -> DoubleLinkedListNode | None:
        if key not in self.__hash:
            return None
        node = self.__hash[key]
        # 此时有效元素个数大于等于1
        if self.__list_dummy_head.next != node:  # 需要移动node
            self.__pop_existing_node_from_list(node)
            self.__insert_existing_node_at_front(node)
        return node

    def __pop_existing_node_from_list(self, node: DoubleLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        # 如果不写，那么仍然存在引用，垃圾永远不会被回收
        node.prev = None
        node.next = None

    def __insert_existing_node_at_front(self, node: DoubleLinkedListNode) -> None:
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
            if len(self.__hash) == self.__capacity:
                node_to_pop = self.__list_dummy_tail.prev
                self.__hash.pop(node_to_pop.key)
                self.__pop_existing_node_from_list(node_to_pop)
            node: DoubleLinkedListNode = DoubleLinkedListNode(key=key, val=value, prev=None, next=None)
            self.__hash[key] = node
            self.__insert_existing_node_at_front(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
