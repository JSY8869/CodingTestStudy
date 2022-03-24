#https://leetcode.com/problems/critical-connections-in-a-network/

###################솔루션 확인####################

#공부한거 바탕으로 설명 쓰긴 했는데 이해할 수 있을지 모르겠네요...
#이해 안되면 스터디때 설명 할게요...

class Solution:
    def criticalConnections(self, n, connections):
        graph = [[] for _ in range(n)]          #연결 상태 그래프
        currentRank = 0                         #현재 몇번째 dfs인지 세줌
        lowestRank = [i for i in range(n)]      #각각의 가장 작은 부모 노드를 담아주는 리스트
        visited = [False for _ in range(n)]
        for connection in connections:          #양방향으로 연결 상태 담아줌
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        
        res = []
        prevVertex = -1         #dfs 들어오기 이전 노드
        currentVertex = 0       #현재 dfs 수행하고 있는 노드
        self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
        
        return res
    
    def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):
        visited[currentVertex] = True               #현재 수행하는 dfs의 노드를 방문처리
        lowestRank[currentVertex] = currentRank     #현재 노드에서 수행중인 dfs가 몇번째인지 저장
        for nextVertex in graph[currentVertex]:     #nextVertex -> 다음으로 갈 노드
            if nextVertex == prevVertex:            #이전 노드(현재 dfs 수행하기 바로 직전 노드)와 다음 노드가 같으면 continue
                continue
            if not visited[nextVertex]:             #다음 노드가 방문하지 않은 노드라면 dfs 수행
                self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)      #dfs를 한번 더 들어가는거니까 currentRank를 1 증가시켜줌
            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])      #dfs를 빠져 나온 뒤, 현재 노드의 랭크 값과
            if lowestRank[nextVertex] == currentRank + 1:                                           #다음 노드의 랭크 값 중 작은 값을 현재 노드의 lowestRank 값으로 바꿔줌
                res.append([currentVertex, nextVertex])     #다음 노드의 랭크 값과 현재 노드의 랭크 값 + 1이 같으면 critical connection
                                                            #dfs가 한바퀴 순환을 다 돌고 나왔다고 생각하면 됨
a = Solution()
print(a.criticalConnections(5, [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]))




##############타잔 알고리즘 깔끔한 솔루션##############

from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:

        graph = defaultdict(list)

        for a, b in connections: # graph 생성
            graph[a].append(b)
            graph[b].append(a)

        t = [float('inf')] * n

        result = []

        '''
        node = 현재 노드
        parent = 부모 노드
        time = 탐색한 시간
        child = 현재 노드에서 이동 가능한 노드
        '''
        def dfs(node, parent, time):  # tarjan 알고리즘
            t[node] = time

            for child in graph[node]: # 한 노드의 연결된 부분들 탐색
                if child == parent:
                    continue
                elif t[child] == float('inf'): # 방문하지 않았다면
                    t[node] = min(t[node], dfs(child, node, time + 1)) # 다음으로 가는것과 가지 않는것 중 빠른걸 저장
                else:
                    t[node] = min(t[node], t[child]) # 방문 했다면 child로 이동해서 가는것과 현재 노드 중 더 빠른 시작점을 저장

            if t[node] == time and parent != -1: # 다른데로 가는 것보다 무조건 최선인 경우
                result.append([parent, node])

            return t[node]

        dfs(0, -1, 0)
        return result