class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # 根据邻接矩阵计算连通分量
        # 无向图的邻接表的右上角（不含对角线有意义），i < j

        city_to_city_is_visited: dict[int, bool] = {}
        for city in range(len(isConnected)):
            city_to_city_is_visited[city] = False

        def visit(city_index: int) -> None:
            city_to_city_is_visited[city_index] = True
            for i in range(len(isConnected)):
                if (((i < city_index and isConnected[i][city_index]) or (i > city_index and isConnected[city_index][i])) and
                        city_to_city_is_visited[i] is False):
                    visit(i)

        n_provinces: int = 0
        for city in range(len(isConnected)):
            if city_to_city_is_visited[city] is False:
                visit(city)
                n_provinces += 1
        return n_provinces
