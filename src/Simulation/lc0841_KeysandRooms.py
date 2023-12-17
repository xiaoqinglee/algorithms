# https://leetcode.cn/problems/keys-and-rooms
class Solution:
    def canVisitAllRooms(self, keys_in_room: list[list[int]]) -> bool:

        visited: list[bool] = [False] * len(keys_in_room)
        visited[0] = True

        rooms_to_open: list[int] = keys_in_room[0]
        while len(rooms_to_open) > 0:
            rooms_to_open_in_next_round: list[int] = []
            for room_id in rooms_to_open:
                visited[room_id] = True
                rooms_to_open_in_next_round += keys_in_room[room_id]
            rooms_to_open = [x for x in rooms_to_open_in_next_round if not visited[x]]

        return all(visited)
