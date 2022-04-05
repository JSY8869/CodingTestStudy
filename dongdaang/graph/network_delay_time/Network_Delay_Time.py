# https://leetcode.com/problems/network-delay-time/


import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        def dijkstra(a):
            d[a] = 0
            heapq.heappush(heap, (0, a))
            while heap:
                time, now = heapq.heappop(heap)         #distance -> 시작점부터 현재 노드까지 걸리는 시간, now -> 현재 위치
                if d[now] < time:
                    continue
                for next, weight in connections[now]:       #next -> 다음 노드, weight -> 두 노드 사이 거리
                    nexttime = d[now] + weight          #nexttime -> 시작점에서부터, 현재 노드의 다음 노드까지 걸리는 시간
                    if d[next] > nexttime:
                        d[next] = nexttime
                        heapq.heappush(heap, (nexttime, next))
        
        connections = [[] for _ in range(n + 1)]        #connections -> 연결 정보(index : 부모 노드, 해당 리스트 : 자식 노드)
        heap = []               #현재 위치에서 가까운 순서로 방문하기 위한 힙 자료구조
        INF = float('inf')      #무한대 표현을 위한 변수
        d = [INF] * (n + 1)     #d -> 시작점에서 현재 위치까지의 최단 시간을 기록해주는 리스트(초기값은 무한대로 설정)
        
        for info in times:
            connections[info[0]].append((info[1], info[2]))
        
        dijkstra(k)
        
        res = max(d[1:])
        if res == INF:
            return -1
        else:
            return res

a = Solution()
print(a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))