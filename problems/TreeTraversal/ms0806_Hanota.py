class Solution:
    def hanota(self, A: list[int], B: list[int], C: list[int]) -> None:

        # 将所有盘子从A移到C

        # (1) 每次只能移动一个盘子
        # (2) 盘子只能从柱子顶端滑出移到下一根柱子
        # (3) 盘子只能叠在比它大的盘子上

        def move(element_count: int, from_: list[int], helper: list[int], to_: list[int]) -> None:

            # 将from_上部分element_count个盘子移动到to_, 移动过程中可以借助helper暂存盘子
            # 这样划分子问题才能满足条件(3)

            if element_count == 1:
                to_.append(from_.pop())
            else:
                move(element_count - 1, from_, to_, helper)
                to_.append(from_.pop())
                move(element_count - 1, helper, from_, to_)

        move(len(A), A, B, C)
