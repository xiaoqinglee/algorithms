class CQueue:
    def __init__(self):
        self.__in_stack: list[int] = []
        self.__out_stack: list[int] = []

    def appendTail(self, value: int) -> None:
        self.__in_stack.append(value)

    def deleteHead(self) -> int:
        if len(self.__out_stack) == 0:
            while len(self.__in_stack) > 0:
                self.__out_stack.append(self.__in_stack.pop())
        if len(self.__out_stack) == 0:
            return -1
        return self.__out_stack.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
