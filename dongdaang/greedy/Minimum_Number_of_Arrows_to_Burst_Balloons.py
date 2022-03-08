#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/


#################솔루션 확인##################

class Solution:
    def findMinArrowShots(self, points):
        points.sort(key = lambda x : x[1])      #끝점을 오름차순으로 정리
        arrows, end = 0, -float('inf')
        for point in points:
            if point[0] > end:                  #끝점을 오름차순으로 정리 했으므로, 현재의 시작점이 저장된 끝점보다
                arrows += 1                     #작기만 하면 같은 화살로 풍선 터뜨리기 가능
                end = point[1]                  #현재 시작점이 저장된 끝점보다 크면, 같은 화살로 터뜨리기 불가능하므로
        return arrows                           #화살수를 하나 늘려주고 끝점을 현재의 끝점으로 설정해줌
    

a = Solution()
print(a.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))