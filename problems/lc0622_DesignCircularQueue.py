from basics.data_structure.CircularQueue import CircularQueue


class MyCircularQueue:
    def __init__(self, k: int):
        self.__queue = CircularQueue(k)

    def enQueue(self, value: int) -> bool:
        return self.__queue.enqueue(value)

    def deQueue(self) -> bool:
        return self.__queue.dequeue()

    def Front(self) -> int:
        try:
            return self.__queue.front()
        except Exception as e:
            return -1

    def Rear(self) -> int:
        try:
            return self.__queue.rear()
        except Exception as e:
            return -1

    def isEmpty(self) -> bool:
        return self.__queue.is_empty()

    def isFull(self) -> bool:
        return self.__queue.is_full()

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
