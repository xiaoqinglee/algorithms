from collections.abc import Callable


class PriorityQueue:
    # https://interviewing.io/questions/build-a-max-heap

    def __init__(self,
                 elements: list[int],
                 has_higher_priority: Callable[[int, int], bool]):
        self.__elements = elements.copy()
        self.__has_higher_priority = has_higher_priority
        # self.__heapify()
        self.__heapify2()

    def __heapify(self) -> None:
        # Time complexity: O(n)
        for element_index in range(self.size() - 1, -1, -1):
            self.__sink_down(element_index)

    def __heapify2(self) -> None:
        # Time complexity: O(n * log(n))
        for element_index in range(self.size()):
            self.__swim_up(element_index)

    def __swim_up(self, element_index: int) -> None:
        while True:
            if element_index == 0:
                break
            index_of_parent = (element_index - 1) // 2
            if self.__has_higher_priority(self.__elements[element_index], self.__elements[index_of_parent]):
                self.__elements[element_index], self.__elements[index_of_parent] = \
                    self.__elements[index_of_parent], self.__elements[element_index]
                element_index = index_of_parent
            else:
                break

    def __sink_down(self, element_index: int) -> None:
        while True:
            child_indexes: list[int] = []
            if 2 * element_index + 1 <= self.size() - 1:
                child_indexes.append(2 * element_index + 1)
            if 2 * element_index + 2 <= self.size() - 1:
                child_indexes.append(2 * element_index + 2)

            if len(child_indexes) == 0:
                break
            index_of_child_with_higher_priority = child_indexes[0]
            if (len(child_indexes) == 2 and
                    self.__has_higher_priority(self.__elements[child_indexes[1]],
                                               self.__elements[child_indexes[0]])):
                index_of_child_with_higher_priority = child_indexes[1]
            if self.__has_higher_priority(self.__elements[index_of_child_with_higher_priority],
                                          self.__elements[element_index]):
                self.__elements[index_of_child_with_higher_priority], self.__elements[element_index] = \
                    self.__elements[element_index], self.__elements[index_of_child_with_higher_priority]
                element_index = index_of_child_with_higher_priority
            else:
                break

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
