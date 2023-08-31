# https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
class Solution:

    # 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
    # 一个机器人从坐标 [0, 0] 的格子开始移动，
    # 它每次可以向左、右、上、下移动一格（不能移动到方格外），
    # 也不能进入行坐标和列坐标的数位之和大于k的格子。
    # 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
    # 但它不能进入方格 [35, 38]，因为3+5+3+8=19。
    # 请问该机器人能够到达多少个格子？

    def movingCount(self, m: int, n: int, k: int) -> int:  # 深度优先搜索（可以选迭代或递归，这里使用递归）

        if m == 0 or n == 0:
            return 0

        result: int = 0
        grid: list[list[str | None]] | None = None

        def digits_sum(row_index: int, col_index: int) -> int:

            def digits_sum_of_integer(int_: int) -> int:
                if int_ == 0:
                    return 0
                digits_sum_of_integer_ = 0
                while int_ != 0:
                    digit = int_ % 10
                    digits_sum_of_integer_ += digit
                    int_ = int_ // 10
                return digits_sum_of_integer_

            return digits_sum_of_integer(row_index) + digits_sum_of_integer(col_index)

        def init_grid() -> None:
            nonlocal grid
            grid = [[None] * n for _ in range(m)]
            for row in range(m):
                for col in range(n):
                    grid[row][col] = "0" if digits_sum(row, col) > k else "1"

        init_grid()

        # '1'（没有访问过的数位之和满足访问要求的位置）和 '0'（数位之和不满足访问要求的位置）
        # '2' (访问过的位置)
        def visit_position(row_index: int, column_index: int) -> None:
            grid[row_index][column_index] = '2'

        def positions_around(row_index: int, column_index: int) -> tuple[tuple[int, int],
                                                                         tuple[int, int],
                                                                         tuple[int, int],
                                                                         tuple[int, int]]:
            return (
                (row_index - 1, column_index),
                (row_index + 1, column_index),
                (row_index, column_index - 1),
                (row_index, column_index + 1)
            )

        def position_is_within_grid(row_index: int, column_index: int) -> bool:
            return 0 <= row_index <= len(grid) - 1 and 0 <= column_index <= len(grid[0]) - 1

        def position_can_be_visited_but_is_not_visited(row_index: int, column_index: int) -> bool:
            return grid[row_index][column_index] == '1'

        def traversal(row_index: int, column_index: int) -> None:
            visit_position(row_index, column_index)
            nonlocal result
            result += 1
            positions_around_ = positions_around(row_index, column_index)
            for r, c in positions_around_:
                if position_is_within_grid(r, c) and position_can_be_visited_but_is_not_visited(r, c):
                    traversal(r, c)

        traversal(0, 0)
        return result
