# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/


class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        horizontalCuts.sort()
        verticalCuts.sort()
        
        new_horizontalCuts = [0] + horizontalCuts + [h]
        new_verticalCuts = [0] + verticalCuts + [w]
        
        max_h, max_w = 0, 0
        
        for i in range(len(new_horizontalCuts) - 1):
            tmp = new_horizontalCuts[i + 1] - new_horizontalCuts[i]
            if tmp > max_h:
                max_h = tmp
                
        for i in range(len(new_verticalCuts) - 1):
            tmp = new_verticalCuts[i + 1] - new_verticalCuts[i]
            if tmp > max_w:
                max_w = tmp
        
        return (max_h * max_w) % ((10 ** 9) + 7)
    
a = Solution()
print(a.maxArea(5, 4, [3], [3]))