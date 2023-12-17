# https://leetcode.cn/problems/zigzag-conversion
def zigzag_conversion(s: str, num_rows: int) -> str:
    if num_rows == 0:
        raise "Invalid input num_rows"
    num_rows = len(s) if len(s) < num_rows else num_rows
    if num_rows <= 1:  # num_rows == 0 或 1
        return s
    rows: list[list[str]] = [[] for x in range(num_rows)]

    current_row: int = 0
    current_direction_is_from_top_to_down: bool = True

    def should_turn_around() -> bool:
        return (current_direction_is_from_top_to_down and current_row == num_rows - 1) or \
               (not current_direction_is_from_top_to_down and current_row == 0)

    for char in s:
        rows[current_row].append(char)
        if should_turn_around():
            current_direction_is_from_top_to_down = not current_direction_is_from_top_to_down
        current_row = current_row + 1 if current_direction_is_from_top_to_down else \
            current_row - 1
    result = ''.join(''.join(row) for row in rows)
    return result
