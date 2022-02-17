from copy import deepcopy

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        board = [['.'] * n for _ in range(n)]
        self.backtracking(n, board, 0, result)
        return result
        
    def backtracking(self, n, board, col, result):
        if col == n: # 체스판 완성
            ret_board = []
            for i in range(n):
                ret_board.append(("".join(board[i]).replace("-", ".")))
            result.append(ret_board)
            return
        for row in range(n):
            if board[col][row] == '.':
                next_board = deepcopy(board)
                self.place_Q(n, next_board, col, row)
                self.backtracking(n, next_board, col+1, result)
                
    def place_Q(self, n, board, y, x): # 가로는 설정할 필요 없음
        i, j = y, x
        while i <= n - 1: # 세로
            board[i][j] = '-'
            i += 1
        i = y
        while i <= n - 1 and j >= 0: # 대각선
            board[i][j] = '-'
            i += 1
            j -= 1
        i, j = y, x
        while i <= n - 1 and j <= n - 1: # 대각선
            board[i][j] = '-'
            i += 1
            j += 1
        board[y][x] = 'Q' # 현재 위치에 퀸 위치