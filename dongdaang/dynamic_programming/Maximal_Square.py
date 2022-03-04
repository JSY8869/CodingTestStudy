#https://leetcode.com/problems/maximal-square/


class Solution:
    def maximalSquare(self, matrix):
        for i in range(len(matrix)):
            matrix[i] = list(map(int, matrix[i]))       #문자 형태의 입력을 숫자로 바꿔줌
        max = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:                   #현 위치가 0이면 정사각형 만들지 못하므로 고려하지 않음
                    continue
                if matrix[i - 1][j] != 0 and matrix[i][j - 1] != 0 and matrix[i - 1][j - 1] != 0:       #현위치에서 왼쪽, 위쪽, 왼쪽위 대각선방향이 모두 0이 아닐 때
                    matrix[i][j] = ((min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) ** 0.5) + 1) ** 2    #셋 중에 가장 작은 값을 이용해 정사각형의 크기 구함
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > max:          #최대값을 찾아주는 과정
                    max = matrix[i][j]
        
        return int(max)         #루트 계산시 실수형으로 변환되어 다시 정수형으로 변환

a = Solution()
print(a.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))





###########################솔루션(위 코드보다 더 간단화, 더 논리적으로 정리된 코드)##############################

class Solution:
    def maximalSquare(self, matrix):
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':     #현 위치 1일때만 고려(정사각형 생성 가능한 위치)
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1    #dp에 현 위치의 왼쪽, 위쪽, 대각선 방향 중 최소값에 1 더한 값을 저장
                                                                                #최소값을 뽑기 때문에 정사각형이 생성될 때 생성된 정사각형의 최소 변의 길이를 알 수 있음
                                                                                #ex) min(2, 2, 1) -> 1 : 크기 9 정사각형 불가, min(2, 2, 2) -> 2 : 크기 9 정사각형 가능
                    max_side = max(max_side, dp[r+1][c+1])      #최대값 중간중간 계속 초기화해줌
                
        return max_side * max_side