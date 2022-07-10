import heapq

Cell = tuple[int, int]


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if len(heightMap) == 0 or len(heightMap[0]) == 0:
            return 0

        # BFS
        # 由边缘向中心慢慢扩散, 每次处理 border cells 中连泥带水高度最小的 cell,
        # 由于没有 dijkstra 的 relax 操作, 所以适合用优先队列.

        def neighbors(cell_: Cell) -> list[Cell]:
            x, y = cell_
            u = x - 1, y
            r = x, y + 1
            d = x + 1, y
            l = x, y - 1
            return [(x, y)
                    for (x, y) in (u, r, d, l)
                    if 0 <= x < len(heightMap) and 0 <= y < len(heightMap[0])]

        # is None: not visited;
        # is not None: cell is visited, and value is water this cell can hold
        trapped_water: list[list[int | None]] = [[None] * len(heightMap[0]) for _ in range(len(heightMap))]
        water_sum: int = 0

        # 最小堆元素是tuple[cell_height, cell], 这个cell_height是该cell盛满水后泥土加水的高度
        visited_border_cells: list[tuple[int, Cell]] = []

        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i in (0, len(heightMap) - 1) or j in (0, len(heightMap[0]) - 1):
                    trapped_water[i][j] = 0
                    visited_border_cells.append((heightMap[i][j], (i, j)))
        heapq.heapify(visited_border_cells)

        while len(visited_border_cells) > 0:
            cell_height, cell = heapq.heappop(visited_border_cells)  # 这个cell_height会慢慢增大, 形成非递减数列
            for neighbor in neighbors(cell):
                i, j = neighbor
                if trapped_water[i][j] is not None:
                    continue

                # visit cell[i][j]
                neighbor_height = heightMap[i][j]
                if neighbor_height < cell_height:
                    trapped_water[i][j] = cell_height - neighbor_height
                    water_sum += trapped_water[i][j]
                    heapq.heappush(visited_border_cells, (cell_height, neighbor))
                else:
                    trapped_water[i][j] = 0
                    heapq.heappush(visited_border_cells, (neighbor_height, neighbor))

        from pprint import pprint
        pprint(heightMap)
        pprint(trapped_water)

        return water_sum
