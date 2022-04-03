#https://leetcode.com/problems/broken-calculator/

class Solution:
    def brokenCalc(self, startValue, target):
        if startValue == target:
            return 0
        elif startValue > target:
            return startValue - target
        else:
            array = []      #array -> startValue에 X 2를 했을 때 가능한 모든 수를 넣어줌
            cnt = 0         #cnt -> 변경 횟수 기록 변수
            while startValue < target:
                array.append(startValue)
                startValue *= 2
            while True:
                if target % 2 == 0:
                    target //= 2
                else:
                    target += 1
                cnt += 1
                if target in array:
                    return cnt + array.index(target)
                if target < array[0]:
                    return cnt + array[0] - target

a = Solution()
print(a.brokenCalc(7, 736))