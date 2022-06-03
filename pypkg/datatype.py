# Definition for singly-linked list.
import collections.abc


class ListNode:
    def __init__(self, val, next=None):
        self.val: int = val
        self.next: ListNode = next


class PriorityHeap:
    def __init__(self,
                 elements: list[int],
                 is_priority: collections.abc.Callable[[int, int], bool]):
        self.__elements = elements.copy()
        self.__is_priority = is_priority
        self.__heapify()

    def __heapify(self) -> None:
        for element_index in range(self.size() - 1, -1, -1):
            self.__sink_down(element_index)

    def __swim_up(self, element_index: int) -> None:
        while True:
            if element_index == 0:
                break
            index_of_parent_to_swap = (element_index - 1) // 2
            if not self.__is_priority(self.__elements[element_index], self.__elements[index_of_parent_to_swap]):
                break
            self.__elements[element_index], self.__elements[index_of_parent_to_swap] = \
                self.__elements[index_of_parent_to_swap], self.__elements[element_index]
            element_index = index_of_parent_to_swap

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
                index_of_child_to_swap = children_indexes[0]
            elif len(children_indexes) == 2:
                index_of_child_to_swap = children_indexes[0] \
                    if self.__is_priority(self.__elements[children_indexes[0]], self.__elements[children_indexes[1]]) \
                    else children_indexes[1]
            if not self.__is_priority(self.__elements[index_of_child_to_swap], self.__elements[element_index]):
                break
            self.__elements[index_of_child_to_swap], self.__elements[element_index] = \
                self.__elements[element_index], self.__elements[index_of_child_to_swap]
            element_index = index_of_child_to_swap

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
