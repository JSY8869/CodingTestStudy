'''
2 는 곱하기 2
1은 빼기 1
startValue에서 target으로 가는 최단 경로
'''
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        count=0

        while target != startValue:

            if target < startValue:
                count += startValue-target # 초과한 만큼 1 빼줘야 함
                break

            elif target % 2 == 1: # target을 움직임
                target += 1

            else:
                target /= 2

            count += 1

        return int(count)






a = Solution()
print(a.brokenCalc(3,10))