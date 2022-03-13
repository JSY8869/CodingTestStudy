class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if len(matrix) == 1 and len(matrix[0]) == 1: # 1칸인 경우 예외처리
            if matrix[0][0] == "1": return 1
            else: return 0

        for i in range(len(matrix)): # int값으로 바꿔줌
            matrix[i] = list(map(int, matrix[i]))

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 1:
                    matrix[row][col] = min(matrix[row-1][col-1], matrix[row-1][col], matrix[row][col-1]) + 1 # 주변에 가장 작은값 + 1이 현재 칸이 만들 수 있는 가장 큰 사각형
                    
        result = 0
        for i in range(len(matrix)):
            result = max(max(matrix[i]), result)
        return result**2 # 가장 큰 값^2




a = Solution()
print(a.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))