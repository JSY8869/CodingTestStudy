from heapq import *

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda x:(x[0],x[1]))
        lists = [] # 종료일
        day = 0 
        result = 0
        for start, end in events:
            while day < start and lists: # 시작할 수 있는 날인가?
                if day <= heappop(lists): # 시작할 게 있는가?
                    day += 1
                    result += 1

            if day < start: # 날짜 이동
                day = start

            heappush(lists, end)
        
        while lists:
            if day <= heappop(lists):
                day += 1
                result += 1
        
        return result





a = Solution()
print(a.maxEvents([[1,2],[2,3],[3,4],[1,2]]))