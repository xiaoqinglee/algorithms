from pprint import pprint


BusId = int
StopId = int


class Solution:
    def numBusesToDestination(self, routes: list[list[StopId]], source: StopId, target: StopId) -> int:
        if source == target:
            return 0
        
        n_buses = len(routes)
        
        # bus作为vertex
        # 可以换乘(存在一个或多个共享的车站)那么两个bus之间存在一条edge
        
        # 由起点bus到终点bus之间最小的edge数
        shortest_path_between_buses: list[list[float]] = [[float("inf")] * n_buses for bus in range(n_buses)]
        middle_buses_in_shortest_path: list[list[list[BusId]]] \
            = [[[] for bus in range(n_buses)] for bus in range(n_buses)]  # 最短路径上不含起点bus和终点bus的bus序列

        stop_to_buses: dict[StopId, list[BusId]] = {}
        for bus_id, stops in enumerate(routes):
            for stop_id in stops:
                stop_to_buses.setdefault(stop_id, []).append(bus_id)
        pprint("车站->车辆关系:")
        pprint(stop_to_buses)

        if source not in stop_to_buses or target not in stop_to_buses:
            return -1

        bus_pair_to_shared_stops: dict[tuple[BusId, BusId], list[StopId]] = {}
        for stop_id, buses in stop_to_buses.items():
            for bus1 in buses:
                for bus2 in buses:  # (15路, 13路)和(13路, 15路)是两个条目, 不存在(13路, 13路)和(15路, 15路)
                    if bus1 == bus2:
                        continue
                    bus_pair_to_shared_stops.setdefault((bus1, bus2), []).append(stop_id)
        pprint("车站对->共享车站:")
        pprint(bus_pair_to_shared_stops)

        # 如果 bus1 == bus2, 我们要排除自环的干扰, 我们让 shortest_path_between_buses[bus1][bus2] == float("inf") 不去管他
        for (bus1, bus2), shared_stops in bus_pair_to_shared_stops.items():
            shortest_path_between_buses[bus1][bus2] = 1
        pprint("shortest_path初始状态:")
        pprint(shortest_path_between_buses)
        pprint("middle_buses_in_shortest_path初始状态:")
        pprint(middle_buses_in_shortest_path)

        for bus1 in range(n_buses):
            for bus2 in range(n_buses):
                for bus3 in range(n_buses):
                    if bus1 == bus2 or bus1 == bus3 or bus2 == bus3:
                        continue
                    if (shortest_path_between_buses[bus1][bus3] + shortest_path_between_buses[bus3][bus2] <
                            shortest_path_between_buses[bus1][bus2]):
                        shortest_path_between_buses[bus1][bus2] = \
                            shortest_path_between_buses[bus1][bus3] + shortest_path_between_buses[bus3][bus2]
                        middle_buses_in_shortest_path[bus1][bus2] = \
                            middle_buses_in_shortest_path[bus1][bus3] + [bus3] + middle_buses_in_shortest_path[bus3][bus2]
        pprint("shortest_path最终状态:")
        pprint(shortest_path_between_buses)
        pprint("middle_buses_in_shortest_path最终状态:")
        pprint(middle_buses_in_shortest_path)

        pprint("=========================================")
        shortest_path: float = float("inf")
        all_buses: list[BusId] = []
        for bus1 in stop_to_buses[source]:
            for bus2 in stop_to_buses[target]:
                if bus1 == bus2:
                    shortest_path = 0
                    all_buses = [bus1]
                    break
                if shortest_path_between_buses[bus1][bus2] < shortest_path:
                    shortest_path = shortest_path_between_buses[bus1][bus2]
                    middle_buses = middle_buses_in_shortest_path[bus1][bus2]
                    all_buses = [bus1] + middle_buses + [bus2]
            if shortest_path == 0:
                break

        if shortest_path != float("inf"):
            if shortest_path == 0:
                pprint(f"一共乘坐1辆公交车:")
                pprint(all_buses)

                pprint("上车车站/换乘车站/下车车站分别为:")
                pprint([[source], [target]])

            else:
                pprint(f"一共乘坐 {shortest_path + 1} 辆公交车:")

                pprint("它们分别为:")
                pprint(all_buses)

                all_stops: list[list[StopId]] = []
                for i, bus in enumerate(all_buses):
                    if i == 0:
                        continue
                    all_stops.append(bus_pair_to_shared_stops[(all_buses[i-1], all_buses[i])])
                pprint("上车车站/换乘车站/下车车站分别为:")
                pprint([[source]] + all_stops + [[target]])
        else:
            pprint("没有可行方案")

        return shortest_path + 1 if shortest_path != float("inf") else -1
