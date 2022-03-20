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




a = Solution()
print(a.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))