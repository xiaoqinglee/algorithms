# https://leetcode.cn/problems/keys-and-rooms
from collections import deque


class Solution:
    def canVisitAllRooms(self, keys_in_room: list[list[int]]) -> bool:

        visited: list[bool] = [False] * len(keys_in_room)
        visited[0] = True

        rooms_to_open: deque[int] = deque(keys_in_room[0])
        while len(rooms_to_open) > 0:
            room_id = rooms_to_open.popleft()
            if not visited[room_id]:
                visited[room_id] = True
                rooms_to_open.extend(keys_in_room[room_id])

        return all(visited)
