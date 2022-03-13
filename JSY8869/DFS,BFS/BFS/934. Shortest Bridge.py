from collections import deque
class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        def dfs(row, col): # 첫 번째 섬을 2로 변경
            grid[row][col] = 2
            q.appendleft((row, col))
            for newRow, newCol in (row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1):  # 4가지 방향를 하나씩 실행
                if 0 <= newRow < n and 0 <= newCol < n and grid[newRow][newCol] == 1:
                    dfs(newRow, newCol)

        n = len(grid)
        q = deque()
        result = 0
        for i in range(n): # 첫번째 섬의 시작점 찾기
            for j in range(n):
                if grid[i][j] == 1:
                    row, col = i, j
        dfs(row, col)

        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.pop()
                for newRow, newCol in (row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1):
                    if 0 <= newRow < n and 0 <= newCol < n:
                        if grid[newRow][newCol] == 0: # 물이면 영토 확장
                            grid[newRow][newCol] = 2
                            q.appendleft((newRow, newCol))
                        elif grid[newRow][newCol] == 1: # 1이면 도착!
                            return result
            result += 1

a = Solution()
print(a.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))