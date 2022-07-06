import heapq


class Solution:

    def isEscapePossible(self,
                         blocked: list[tuple[int, int]],
                         source: tuple[int, int],
                         target: tuple[int, int]) -> bool:
        # 原输入中的point是无法hash的两个元素的list
        blocked = set(tuple(li) for li in blocked)
        source = tuple(source)
        target = tuple(target)

        if len(blocked) == 0:
            return True

        def neighbors(position: tuple[int, int]) -> list[tuple[int, int]]:
            x, y = position
            u = x - 1, y
            r = x, y + 1
            d = x + 1, y
            l = x, y - 1
            return [(x, y)
                    for (x, y) in (u, r, d, l)
                    if 0 <= x < 1000000 and 0 <= y < 1000000 and (x, y) not in blocked]

        def heuristic_func(next: tuple[int, int], target: tuple[int, int]) -> int:
            # Manhattan distance on a square grid
            return abs(next[0] - target[0]) + abs(next[1] - target[1])

        cost_so_far: dict[tuple[int, int], int] = {}
        came_from: dict[tuple[int, int], tuple[int, int]] = {}
        # next_position_candidates 的元素是 tuple[priority, tuple[x, y]]
        next_position_candidates: list[tuple[int, tuple[int, int]]] = []

        cost_so_far[source] = 0
        came_from[source] = source
        # 最小堆, 成本越低越优先
        next_position_candidates.append((0, source))

        current: tuple[int, int] = None
        while len(next_position_candidates) > 0:

            _, current = heapq.heappop(next_position_candidates)
            print(current)

            if current == target:
                break

            for next_ in neighbors(current):
                next_pos_cost = cost_so_far[current] + 1
                # 如果 next_ 还未被推入堆,
                # 或 next_ 已被推入堆或 next_ 之前已被被访问过但是经由 current 访问 next 我们能得到更小的成本,
                # 这导致 next_ 重新被考虑
                if next_ not in cost_so_far or next_pos_cost < cost_so_far[next_]:
                    cost_so_far[next_] = next_pos_cost
                    priority = next_pos_cost + heuristic_func(next_, target)
                    heapq.heappush(next_position_candidates, (priority, next_))
                    came_from[next_] = current

        return current == target


# https://www.redblobgames.com/pathfinding/a-star/introduction.html
