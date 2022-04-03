class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        
        while len(matrix) > 0: # 돌려돌려 돌림판!
            result += list(matrix.pop(0))
            matrix = list(zip(*matrix))
            matrix.reverse()
    
        return result
a = Solution()
print(a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))