#https://leetcode.com/problems/shortest-path-with-alternating-colors/


from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        def bfs():
            queue = deque(graph[0])
            while queue:
                node, color, d = queue.popleft()
                if distance[node] == -1:
                    distance[node] = d
                for edge in graph[node]:
                    if edge[1] != color and visited[node][edge[0]] < 2:
                        visited[node][edge[0]] += 1
                        queue.append((edge[0], edge[1], d + 1))
            
        graph = [[] for _ in range(n)]      #연결 상태 저장할 2차원 배열
        distance = [-1] * n     #최종 거리 값이 저장될 리스트
        distance[0] = 0
        visited = [[0] * n for _ in range(n)]       #방문 처리를 위한 2차원 배열
        for edge in redEdges:
            graph[edge[0]].append((edge[1], 0, 1))
        for edge in blueEdges:
            graph[edge[0]].append((edge[1], 1, 1))
            
        bfs()
                
        return distance
    
a = Solution()
print(a.shortestAlternatingPaths(6, [[4,1],[3,5],[5,2],[1,4],[4,2],[0,0],[2,0],[1,1]], [[5,5],[5,0],[4,4],[0,3],[1,0]]))