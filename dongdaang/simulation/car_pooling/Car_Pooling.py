# https://leetcode.com/problems/car-pooling/

import heapq

class Solution:
    def carPooling(self, trips, capacity):
        trips.sort(key=lambda x : x[1])
        if trips[0][0] > capacity:
            return False
        
        n = len(trips)
        heap = [(trips[0][2], trips[0][0])]
        total = trips[0][0]
        
        for i in range(1, n):
            people, start, end = trips[i]
            while heap:
                if heap[0][0] <= start:
                    tmp = heapq.heappop(heap)
                    total -= tmp[1]
                else:
                    break
            
            total += people
            if total <= capacity:
                heapq.heappush(heap, (end, people))
            else:
                return False
        
        return True

a = Solution()
print(a.carPooling([[2,1,5],[3,3,7]], 4))