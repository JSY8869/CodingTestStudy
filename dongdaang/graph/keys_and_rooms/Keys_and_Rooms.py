#https://leetcode.com/problems/keys-and-rooms/


class Solution:
    def canVisitAllRooms(self, rooms):
        def dfs(key):
            visited[key] = True
            for i in rooms[key]:
                if not visited[i]:
                    dfs(i)
        
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        
        for key in rooms[0]:
            dfs(key)
        
        return all(visited)

a = Solution()
print(a.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))