
class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        min_index = slices.index(min(slices))
        slices = slices[min_index+1:] + slices[0:min_index+1] # 제일 작은 값 뒤에 + 제일 작은 값 까지
        
        total, n = len(slices), len(slices) / 3
        n = int(n)
        dp = [[0] * (total+1)] * (n+1)
        print(dp)
        for r in range(n):
            for c in range(r, total):
                dp[r][c] = max(slices[c] + dp[r-1][c-2], dp[r][c-1])
        return dp[-2][-2]


a = Solution()
a.maxSizeSlices([8,9,1,6,5,1])
