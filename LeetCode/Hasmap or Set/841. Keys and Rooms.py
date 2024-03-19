from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = {0: True}
        keys = rooms[0]

        while keys:
            current_key = keys.pop()
            if not current_key in visited_rooms:
                visited_rooms[current_key] = True
                keys.extend(rooms[current_key])
        
        for i in range(len(rooms)):
            if i not in visited_rooms:
                return False
        return True

        