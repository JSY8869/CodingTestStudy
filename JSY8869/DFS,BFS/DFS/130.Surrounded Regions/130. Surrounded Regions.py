class Solution(object):
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j): # 경계선과 연결된 O를 M으로 바꿀 때 사용
            
            if not (0<=i<m) or not (0<=j<n) or board[i][j] != 'O': # 범위 초과 or 이미 체크한 경우
                return
            
            board[i][j] = 'M'

            dfs(board, i-1, j)
            dfs(board, i+1, j)
            dfs(board, i, j-1)
            dfs(board, i, j+1)
            

        m = len(board) # 세로 길이
        n = len(board[0]) # 가로 길이

        #Search from the 'o' of the boundary
        for i in range(m):
            for j in range(n):
                is_frontier = (i == 0 or j == 0 or i == m-1 or j == n-1) # 경계선인 경우 True
                if is_frontier and board[i][j] == 'O':
                    dfs(board, i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': # 경계선과 연결되지 않은 O를 X로 바꿈
                    board[i][j] = 'X'
                if board[i][j] == 'M': # 경계선과 연결된 O를 다시 O로 바꿔줌
                    board[i][j] = 'O'
        
board = [['X','x', 'X'],
        ['X', 'O', 'X'],
        ['X', 'O', 'X'],
        ['X', 'O', 'X']]
a = Solution()
a.solve(board)