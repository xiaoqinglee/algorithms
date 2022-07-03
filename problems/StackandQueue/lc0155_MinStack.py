class MinStack:

    def __init__(self):
        # element is tuple(ElementValue, MinElementValue)
        self.__list: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        min_ = min(val, self.getMin()) if len(self.__list) > 0 else val
        self.__list.append((val, min_))

    def pop(self) -> None:
        if len(self.__list) == 0:
            raise "Empty MinStack"
        self.__list.pop()

    def top(self) -> int:
        if len(self.__list) == 0:
            raise "Empty MinStack"
        return self.__list[-1][0]

    def getMin(self) -> int:
        if len(self.__list) == 0:
            raise "Empty MinStack"
        return self.__list[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
