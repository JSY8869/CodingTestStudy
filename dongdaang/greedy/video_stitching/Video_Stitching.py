# https://leetcode.com/problems/video-stitching/


class Solution:
    def videoStitching(self, clips, time):
        clips.sort()
        
        if clips[0][0] != 0:
            return -1
        
        N = len(clips)
        used = [False] * N      #사용된 clip 표시를 위한 리스트
        covered = clips[0]      #현재까지 커버된 video 파트
        used[0] = True
        res = 0
        
        for i in range(1, N):
            if covered[1] >= time:
                break
            if clips[i][1] > covered[1] and clips[i][0] <= covered[1]:
                covered = [0, clips[i][1]]
                used[i] = True
                for j in range(i):
                    if used[j]:
                        if clips[j][0] == clips[i][0]:
                            for k in range(j, i):
                                used[k] = False
                        elif clips[j][0] < clips[i][0] <= clips[j][1]:
                            for k in range(j + 1, i):
                                used[k] = False
        
        if covered[1] < time:
            return -1
        
        res = used.count(True)
        
        return res

a = Solution()
print(a.videoStitching([[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]], 5))


##############솔루션################

# def videoStitching(self, clips, T):
#     end, end2, res = -1, 0, 0
#     for i, j in sorted(clips):
#         if end2 >= T or i > end2:
#             break
#         elif end < i <= end2:
#             res, end = res + 1, end2
#         end2 = max(end2, j)
#     return res if end2 >= T else -1