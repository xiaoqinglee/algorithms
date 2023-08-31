# https://leetcode.cn/problems/spiral-matrix
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        result: list[int] = []

        # 1: True 0: False
        visited: list[list[int]] = [[0] * len(matrix[0]) for x in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited[i][j] = 0

        # directions: list[str] = ("right", "down", "left", "up")
        current_direction: int = 0
        current_position: tuple[int, int] = (0, 0)

        def position_indexes_is_valid(row_index: int, col_index: int) -> bool:
            return 0 <= row_index < len(matrix) and 0 <= col_index < len(matrix[0])

        def turn_right() -> None:
            nonlocal current_direction
            current_direction = (current_direction + 1) % 4

        def next_position() -> tuple[int, int]:
            if current_direction == 0:
                front_position = (current_position[0], current_position[1] + 1)
            elif current_direction == 1:
                front_position = (current_position[0] + 1, current_position[1])
            elif current_direction == 2:
                front_position = (current_position[0], current_position[1] - 1)
            else:  # current_direction == 3
                front_position = (current_position[0] - 1, current_position[1])
            return front_position

        def move_position() -> None:
            nonlocal current_position
            current_position = next_position()

        def need_turn_right() -> bool:
            front_position: tuple[int, int] = next_position()
            if position_indexes_is_valid(front_position[0], front_position[1]) and \
                    visited[front_position[0]][front_position[1]] == 0:
                return False
            return True

        element_count: int = len(matrix) * len(matrix[0])
        for i in range(element_count):
            visited[current_position[0]][current_position[1]] = 1
            result.append(matrix[current_position[0]][current_position[1]])
            if i < element_count - 1:
                if need_turn_right():
                    turn_right()
                move_position()

        return result
