from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        result = 0
        for start, destination, time in times:
            graph[start].append((time, destination))

        heap = [(0,k)]

        while heap:
            nowTime, now = heapq.heappop(heap)
            
            if now in visited:
                continue

            visited.add(now)
            
            result = nowTime

            for nextTime, nextNode in graph[now]:
                heapq.heappush(heap, (nextTime + nowTime, nextNode))

        if len(visited) != n:
            return -1
        return result


a = Solution()
print(a.networkDelayTime([[2,4,10],[5,2,38],[3,4,33],[4,2,76],[3,2,64],[1,5,54],[1,4,98],[2,3,61],[2,1,0],[3,5,77],[5,1,34],[3,1,79],[5,3,2],[1,2,59],[4,3,46],[5,4,44],[2,5,89],[4,5,21],[1,3,86],[4,1,95]],5,1))