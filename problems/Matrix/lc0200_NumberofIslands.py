class Solution:

    # 岛屿数量就是开始一次深度有限搜素或广度优先搜索的次数，是森林中树的个数

    # def numIslands(self, grid: list[list[str]]) -> int:  # 广度优先搜索（使用队列）
    #
    #     if len(grid) == 0 or len(grid[0]) == 0:
    #         return 0
    #
    #     # '1'（没有访问过的陆地）和 '0'（水）
    #     # '2' (访问过的陆地)
    #     def visit_position(row_index: int, column_index: int) -> None:
    #         grid[row_index][column_index] = '2'
    #
    #     def positions_around(row_index: int, column_index: int) -> tuple[tuple[int, int],
    #                                                                      tuple[int, int],
    #                                                                      tuple[int, int],
    #                                                                      tuple[int, int]]:
    #         return (
    #             (row_index - 1, column_index),
    #             (row_index + 1, column_index),
    #             (row_index, column_index - 1),
    #             (row_index, column_index + 1)
    #         )
    #
    #     def position_is_in_grid(row_index: int, column_index: int) -> bool:
    #         return 0 <= row_index <= len(grid) - 1 and 0 <= column_index <= len(grid[0]) - 1
    #
    #     def position_is_not_visited_land(row_index: int, column_index: int) -> bool:
    #         return grid[row_index][column_index] == '1'
    #
    #     def traversal(row_index: int, column_index: int) -> None:
    #         queue.append((row_index, column_index))
    #         while len(queue) >= 1:
    #             position: tuple[int, int] = queue.popleft()
    #             visit_position(position[0], position[1])
    #             positions_around_: list[tuple[int, int]] = positions_around(position[0], position[1])
    #             for r, c in positions_around_:
    #                 if position_is_in_grid(r, c) and position_is_not_visited_land(r, c):
    #                     queue.append((r, c))
    #
    #     from collections import deque
    #     queue: deque[tuple[int, int]] = deque()
    #
    #     n_islands: int = 0
    #     for row_idx in range(len(grid)):
    #         for col_idx in range(len(grid[0])):
    #             if position_is_not_visited_land(row_idx, col_idx):
    #                 traversal(row_idx, col_idx)
    #                 n_islands += 1
    #     return n_islands

    def numIslands(self, grid: list[list[str]]) -> int:  # 深度优先搜索（可以选迭代或递归，这里使用递归）

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        # '1'（没有访问过的陆地）和 '0'（水）
        # '2' (访问过的陆地)
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

        def position_is_in_grid(row_index: int, column_index: int) -> bool:
            return 0 <= row_index <= len(grid) - 1 and 0 <= column_index <= len(grid[0]) - 1

        def position_is_not_visited_land(row_index: int, column_index: int) -> bool:
            return grid[row_index][column_index] == '1'

        # 代码从这里向后开始不一样了
        def traversal(row_index: int, column_index: int) -> None:
            visit_position(row_index, column_index)
            positions_around_ = positions_around(row_index, column_index)
            for r, c in positions_around_:
                if position_is_in_grid(r, c) and position_is_not_visited_land(r, c):
                    traversal(r, c)

        # 不同的地方结束
        n_islands: int = 0
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if position_is_not_visited_land(row_idx, col_idx):
                    traversal(row_idx, col_idx)
                    n_islands += 1
        return n_islands
