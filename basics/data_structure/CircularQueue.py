class CircularQueue:
    def __init__(self, capacity: int):
        self.__capacity: int = capacity
        self.__len: int = 0  # 需要这个变量来区分首尾指针重合在一起的情况是空状态还是满状态
        self.__lst: list[int | None] = [None] * capacity
        self.__index_to_write_to: int = 0  # 走得快，是队尾
        self.__index_to_read_from: int = 0  # 走得慢，是队头

    def __len__(self) -> int:
        return self.__len

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        self.__lst[self.__index_to_write_to] = value
        self.__index_to_write_to = (self.__index_to_write_to + 1) % self.__capacity
        self.__len += 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self.__index_to_read_from = (self.__index_to_read_from + 1) % self.__capacity
        self.__len -= 1
        return True

    def front(self) -> int:
        if self.is_empty():
            raise "Empty Queue"
        return self.__lst[self.__index_to_read_from]

    def rear(self) -> int:
        if self.is_empty():
            raise "Empty Queue"
        return self.__lst[(self.__index_to_write_to - 1 + self.__capacity) % self.__capacity]

    def is_empty(self) -> bool:
        return self.__len == 0

    def is_full(self) -> bool:
        return self.__len == self.__capacity
