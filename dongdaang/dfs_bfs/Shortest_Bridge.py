#https://leetcode.com/problems/shortest-bridge/


#1. dfs로 2개의 대륙 중 하나만 찾음
#2. 찾은 대륙에서 bfs를 통해 또 다른 대륙까지의 거리 측정

from collections import deque

class Solution:
    def shortestBridge(self, grid):
        N = len(grid)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque()
        
        def dfs(x, y):
            grid[x][y] = -1         #dfs를 수행할 때, 이미 방문한 위치는 -1로 변경
            queue.append((x, y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                    dfs(nx, ny)
                    
        def bfs():
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N or grid[nx][ny] == -1:        #이동할 위치가 범위 밖이거나 해당 값이 -1인 경우 continue
                        continue   
                    if grid[nx][ny] != 1 and grid[nx][ny] != 0: #도착지이가 아니거나 0이 아니면 방문할 필요 없으므로 continue
                        continue
                    if grid[nx][ny] == 1:                       #값이 1이면 다른 대륙에 도착한 것을 의미하므로 값을 리턴
                        return abs(grid[x][y]) - 1              #거리 값을 빼주면서 전진했기 때문에 반환 값은 절댓값(해당 위치 값) - 1
                    elif grid[nx][ny] == 0:                     #값이 0이면 계속 진행
                        grid[nx][ny] = grid[x][y] - 1           #거리 값을 빼주면서 전진
                        queue.append((nx, ny))

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    dfs(i, j)           #dfs를 한번만 수행하고 바로 bfs 수행
                    return bfs()

a = Solution()
print(a.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))