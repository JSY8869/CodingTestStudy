#https://leetcode.com/problems/gas-station/


##############솔루션 확인##############

class Solution:
    def canCompleteCircuit(self, gas, cost):
        n, total, tmp, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total += gas[i] - cost[i]
            tmp += gas[i] - cost[i]
            if tmp < 0:             #지금까지 오는데 연료 다 소진되면
                tmp = 0             #0으로 초기화
                start = i + 1       #이 지점 앞에서는 출발 못함(이 지점까지 오는데 결국 연료 다 소진될 것이므로)
        return -1 if (total < 0) else start

a = Solution()
print(a.canCompleteCircuit([2,0,1,2,3,4,0], [0,1,0,0,0,0,11]))