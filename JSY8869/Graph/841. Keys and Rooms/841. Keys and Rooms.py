from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        q = deque()
        q.append(rooms[0])
        visited = [0]

        while q:
            keys = q.pop()
            for key in keys:
                if key in visited:
                    continue
                visited.append(key)
                q.append(rooms[key])

        return len(visited) == len(rooms)


a = Solution()
print(a.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))