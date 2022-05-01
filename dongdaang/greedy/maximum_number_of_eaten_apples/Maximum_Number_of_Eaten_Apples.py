#https://leetcode.com/problems/maximum-number-of-eaten-apples/


import heapq

class Solution:
    def eatenApples(self, apples, days):
        n = len(days)
        heap = []       #사과 담을 힙
        apple_cnt = 0   #먹은 사과 개수
        day_cnt = 0     #지난 날짜 수
        
        for i in range(n):      #사과를 수확할 수 있는 경우
            heapq.heappush(heap, (days[i] + i, apples[i]))
            while heap:
                now = heapq.heappop(heap)
                if now[0] - day_cnt > 0 and now[1] > 0:
                    next = (now[0], now[1] - 1)
                    if next[1] > 0:
                        heapq.heappush(heap, next)
                    apple_cnt += 1
                    break
            day_cnt += 1
        
        while heap:     #모든 사과 수확 후 남은 사과 먹는 경우
            while heap:
                now = heapq.heappop(heap)
                if now[0] - day_cnt > 0 and now[1] > 0:
                    next = (now[0], now[1] - 1)
                    if next[1] > 0:
                        heapq.heappush(heap, next)
                    apple_cnt += 1
                    break
            day_cnt += 1
        
        return apple_cnt
    
a = Solution()
print(a.eatenApples([2,1,1,4,5], [10,10,6,4,2]))