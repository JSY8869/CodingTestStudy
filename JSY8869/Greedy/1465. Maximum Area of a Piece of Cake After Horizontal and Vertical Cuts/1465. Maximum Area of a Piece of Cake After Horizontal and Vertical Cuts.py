
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.sort()
        horizontalCuts.append(h)
        Max_H = horizontalCuts[0]

        verticalCuts.sort()
        verticalCuts.append(w)
        Max_V = verticalCuts[0]

        for i in range(len(horizontalCuts)-1):
            Max_H = max(horizontalCuts[i+1] - horizontalCuts[i], Max_H)

        for i in range(len(verticalCuts)-1):
            Max_V = max(verticalCuts[i+1] - verticalCuts[i], Max_V)
            
        return (Max_H*Max_V%int(1e9 + 7))
            

a = Solution()
print(a.maxArea(1000000000, 1000000000, [2] ,[2]))