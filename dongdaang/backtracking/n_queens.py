#######################솔루션 확인########################
class Solution:
    def solveNQueens(self, n):
        col = [0] * (n + 1)            #인덱스 : 행 번호, 값 : 열 번호
        result = []
        ans = []
        
        def promising(i, col):         #현재 퀸의 위치가 가능한지 판단해주는 함수
            k = 1
            flag = True
            while(k < i and flag):
                if col[i] == col[k] or abs(col[i] - col[k]) == i - k:       #같은 열이거나 대각선에 위치하면 False
                    flag = False
                k += 1
            return flag

        def n_queens(i, col):
            if promising(i, col):           #퀸이 유망하지 않다면 백트래킹
                if i == n:
                    result.append(col[1:n + 1])         #최대 깊이까지 탐색 했으면 정답이므로 result에 추가
                else:
                    for j in range(1, n + 1):           #최대 깊이가 아니라면 다음 행에 퀸을 하나씩 두고 dfs 적용
                        col[i + 1] = j
                        n_queens(i + 1, col)
        n_queens(0, col)
        
        #정답 형태 맞추기 위한 단순 작업
        for i in result:
            graph = [['.' for _ in range(n)] for _ in range(n)]
            tmp = []
            for j in range(n):
                graph[j][i[j]-1] = 'Q'
            for i in range(n):
                s = ''
                for j in range(n):
                    s += graph[i][j]
                tmp.append(s)
            ans.append(tmp)
        return ans

a = Solution()
print(a.solveNQueens(4))