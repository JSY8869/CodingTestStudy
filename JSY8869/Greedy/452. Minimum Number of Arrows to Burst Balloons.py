class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points, key = lambda x: x[1]) # 끝을 기준으로 오름차순 정렬
        result = 0
        now = float("-inf") # 음의 무한대
        for i in range(len(points)):
            if now < points[i][0]: # now보다 시작이 크면 화살 더 필요함
                result += 1
                now = points[i][1] # 이번 풍선의 끝을 now로 저장
        return result


a = Solution()
print(a.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))