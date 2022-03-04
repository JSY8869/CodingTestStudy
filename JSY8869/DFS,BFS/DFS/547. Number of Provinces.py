from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        
        graph = defaultdict(list) # key 값이 없는 경우 default값으로 지정

        n = len(isConnected)

        for i in range(n): # 그래프 생성
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = [False]*n
        
        def dfs(now):
            for next in graph[now]:
                if visited[next] == False:
                    visited[next] = True # 방문 처리
                    dfs(next)
        
        count = 0
        for i in range(n):
            print(visited)
            if visited[i] == False:
                count += 1
                visited[i] = True
                dfs(i)
        
        return count
a = Solution()
print(a.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))