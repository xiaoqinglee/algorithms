from pprint import pprint


BusId = int
StopId = int
Change = list[StopId]
SuccessiveChanges = list[Change]


class Solution:
    def numBusesToDestination(self, routes: list[list[StopId]], source: StopId, target: StopId) -> int:
        if source == target:
            return 0

        n_buses = len(routes)
        successive_n_changes_min: list[list[float]] = [[float("inf")] * n_buses for bus in range(n_buses)]
        successive_changes_detail: list[list[SuccessiveChanges]] \
            = [[[] for bus in range(n_buses)] for bus in range(n_buses)]
        stop_to_buses: dict[StopId, list[BusId]] = {}
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses.setdefault(stop, []).append(bus)
        # pprint(stop_to_buses)

        if source not in stop_to_buses or target not in stop_to_buses:
            return -1

        for stop, buses in stop_to_buses.items():
            for i, bus1 in enumerate(buses):
                for bus2 in buses[i:]:
                    successive_n_changes: float = successive_n_changes_min[bus1][bus2]
                    if bus1 == bus2:
                        successive_n_changes_min[bus1][bus2] = 0.0
                    else:
                        if successive_n_changes == float("inf"):
                            successive_n_changes_min[bus1][bus2] = 1.0
                            successive_n_changes_min[bus2][bus1] = 1.0
                            successive_changes_detail[bus1][bus2].append([])
                            successive_changes_detail[bus2][bus1].append([])
                        successive_changes_detail[bus1][bus2][0].append(stop)
                        successive_changes_detail[bus2][bus1][0].append(stop)
        # pprint(successive_n_changes_min)
        # pprint(successive_changes_detail)

        for bus1 in range(n_buses):
            for bus2 in range(n_buses):
                for bus3 in range(n_buses):
                    if bus1 == bus2 or bus1 == bus3 or bus2 == bus3:
                        continue
                    if (successive_n_changes_min[bus1][bus3] + successive_n_changes_min[bus3][bus2] <
                            successive_n_changes_min[bus1][bus2]):
                        successive_n_changes_min[bus1][bus2] = \
                            successive_n_changes_min[bus1][bus3] + successive_n_changes_min[bus3][bus2]
                        successive_changes_detail[bus1][bus2] = \
                            successive_changes_detail[bus1][bus3] + successive_changes_detail[bus3][bus2]

        # pprint(successive_n_changes_min)
        # pprint(successive_changes_detail)

        n_min: float = float("inf")
        n_changes_in_detail: SuccessiveChanges = None
        for bus1 in stop_to_buses[source]:
            for bus2 in stop_to_buses[target]:
                if successive_n_changes_min[bus1][bus2] < n_min:
                    n_min = successive_n_changes_min[bus1][bus2]
                    n_changes_in_detail = successive_changes_detail[bus1][bus2]

        return int(n_min) + 1 if n_min != float("inf") else -1
