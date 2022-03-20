#https://leetcode.com/problems/longest-increasing-subsequence/


###############dp 활용(2971ms)#################
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [0] * n
        
        for i in range(n):                                  #하나씩 전진
            for j in range(i):                              #처음부터 현재 위치까지 비교
                if nums[i] > nums[j] and dp[i] < dp[j]:     #현재 숫자가 이전 숫자보다 크고, 현재 위치 dp값이 더 작으면
                    dp[i] += 1                              #dp를 하나 증가(dp값을 따지는 이유 : 숫자 값만 비교하면 증가하는 수열을 파악할 수 없음)
            dp[i] += 1                                      #dp은 현재까지 증가 수열의 최대값을 담고 있는 개념
        return max(dp)                                      #앞에서 자기보다 작은 수만 따져 왔으니까 마지막에 현재 dp에 1 더해줌
    
a = Solution()
print(a.lengthOfLIS([0,1,0,3,2,3]))



################이진 탐색 활용 솔루션(110ms)################
class Solution:
    def lengthOfLIS(self, nums):        #증가하는 부분수열의 마지막 값을 저장해줌
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:       #이진 탐색으로 마지막 값을 저장할 위치 찾아줌
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x            #그 위치에 마지막 값 저장
            size = max(i + 1, size)         #저장한 값의 size가 정답
        return size
a = Solution()
print(a.lengthOfLIS([4,11,12,13,9,5,3,14,101,102,18,6,7,8,9,10]))