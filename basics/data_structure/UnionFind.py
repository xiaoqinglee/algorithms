from typing import Any


ImmutableComparableElem = Any


class UnionFind:
    # 一个UnionFind中存储着多个集合，每个集合有一个代表，这个代表是这个集合的名片
    def __init__(self,
                 from_vertexes: list[ImmutableComparableElem] | None = None,
                 from_edges: list[tuple[ImmutableComparableElem, ImmutableComparableElem]] | None = None):
        self.follows: dict[ImmutableComparableElem, ImmutableComparableElem] = {}
        if from_vertexes:
            self.init_with_free_elements(from_vertexes)
            return
        if from_edges:
            self.init_with_linked_element_pairs(from_edges)
            return

    def init_with_free_elements(self, elems: list[ImmutableComparableElem]) -> None:
        for elem in elems:
            if elem not in self.follows:
                self.follows[elem] = elem

    def init_with_linked_element_pairs(self,
                                       elem_pairs: list[tuple[ImmutableComparableElem, ImmutableComparableElem]]) \
            -> None:
        for elem1, elem2 in elem_pairs:
            if elem1 not in self.follows:
                self.follows[elem1] = elem1
            if elem2 not in self.follows:
                self.follows[elem2] = elem2
            self.union(elem1, elem2)

    # 元素填充完毕之后才可以使用
    def belongs_to_same_set(self, elem1: ImmutableComparableElem, elem2: ImmutableComparableElem) -> bool:
        return self.find(elem1) == self.find(elem2)

    # 元素填充完毕之后才可以使用
    def find(self, elem: ImmutableComparableElem) -> ImmutableComparableElem:
        followed = self.follows[elem]
        if followed == elem:
            return elem
        representative = self.find(followed)
        self.follows[elem] = representative  # 路径压缩
        return representative

    # 元素填充完毕之后才可以使用
    def union(self, elem1: ImmutableComparableElem, elem2: ImmutableComparableElem) -> None:
        set1_rep = self.find(elem1)
        set2_rep = self.find(elem2)
        if set1_rep == set2_rep:
            return
        elif set1_rep < set2_rep:
            self.follows[set2_rep] = set1_rep
        else:
            self.follows[set1_rep] = set2_rep
