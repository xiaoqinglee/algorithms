# https://leetcode.cn/problems/number-of-provinces
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # 根据邻接矩阵计算连通分量
        # 无向图的邻接表
        # 题目保证了 isConnected[i][j] == isConnected[j][i]

        city_count = len(isConnected)
        city_is_visited: dict[int, bool] = {}
        for city in range(city_count):
            city_is_visited[city] = False

        # 要求调用者保证 city_is_visited[city_index] == False
        def visit(city_index: int) -> None:
            city_is_visited[city_index] = True
            for city_adj in range(city_count):
                if city_adj == city_index:
                    continue
                if city_is_visited[city_adj] is True:
                    continue
                if isConnected[city_index][city_adj]:
                    visit(city_adj)

        n_provinces: int = 0
        for city in range(city_count):
            if city_is_visited[city] is False:
                visit(city)
                n_provinces += 1
        return n_provinces
