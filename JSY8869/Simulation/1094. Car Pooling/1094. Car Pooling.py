class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        start = []
        end = []
        passenger = 1
        point = 0
        for p,s,e in trips:
            start.append([s,p])
            end.append([e,p])
        start.sort()
        end.sort()
        start_index = 0
        end_index = 0
        while start_index < len(trips) and end_index < len(trips):
            if start[start_index][point] < end[end_index][point]:
                capacity -= start[start_index][passenger]
                if capacity < 0:
                    return False
                start_index += 1
            else:
                capacity += end[end_index][passenger]
                end_index += 1
        return True
            



a = Solution()
a.carPooling([[3,3,7],[2,1,5]], 4)