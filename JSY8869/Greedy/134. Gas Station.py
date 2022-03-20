class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        result = 0
        left_gas = 0
        if sum(gas) < sum(cost): # 예외
            return -1
        for index in range(len(gas)):
            left_gas += gas[index] - cost[index] # 남은 가스 =  남은 가스 + 충전할 가스 - 비용
            if left_gas < 0:
                result = index+1
                left_gas = 0
        return result

    

a = Solution()
print(a.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
