class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]: # 증가 되는 경우
                    dp[i] = max(dp[i], 1 + dp[j]) # j로 가서 시작하는것과 i에서 시작하는 것 비교
        return max(dp)

a = Solution()
print(a.lengthOfLIS([10,9,2,5,3,7,101,18]))