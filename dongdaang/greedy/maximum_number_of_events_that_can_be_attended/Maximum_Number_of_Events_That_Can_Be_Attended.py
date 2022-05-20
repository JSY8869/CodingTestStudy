# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/


import heapq
from collections import defaultdict

class Solution:
    def maxEvents(self, events):
        events.sort()
        
        dates = defaultdict(int)    #이벤트가 시작하는 날짜를 저장하는 딕셔너리
        last_date = 0               #이벤트가 진행될 수 있는 마지막 날
        res = 0
        index = 0
        heap = []                   #현재 참여할 수 있는 이벤트를 저장하는 heap
        
        for event in events:
            dates[event[0]] += 1
            if event[1] > last_date:
                last_date = event[1]

        for date in range(1, last_date + 1):
            if date in dates.keys():
                for i in range(index, index + dates[date]):
                        heapq.heappush(heap, (events[i][1], events[i]))
                index += dates[date]
            while heap:
                current_meeting = heapq.heappop(heap)
                if current_meeting[1][0] <= date <= current_meeting[1][1]:
                    res += 1
                    break
                    
        return res

a = Solution()
print(a.maxEvents([[1,3], [1,3], [1,3], [3,4]]))