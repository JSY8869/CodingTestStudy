
class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        dp = [time+1]*(time+1)
        dp[0] = 0

        for now in range(time+1):

            for clip in clips:
                if now >= clip[0] and now <= clip[1]: # 현재 clip의 해당하는 시간인 경우
                    dp[now] = min(dp[now], dp[clip[0]]+1) # 둘 중 더 빠른 경로 선택

            if dp[now] == time+1: # 완성 실패
                return -1

        return dp[-1]

        
a = Solution()
a.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]],10)