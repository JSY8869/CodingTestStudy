from copy import deepcopy

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ret = []
        board = [['.'] * n for _ in range(n)]
        self.backtracking(n, board, 0, ret)
        return ret
        
    def backtracking(self, n, board, num_Q, ret):
        if num_Q == n:
            ret_board = []
            for i in range(n):
                temp = list(board[i])
                for j in range(len(temp)):
                    if temp[j] != 'Q':
                        temp[j] = '.'
                ret_board.append(''.join(temp))
            ret.append(ret_board)
            return
        for i in range(n):
            if board[num_Q][i] == '.':
                next_board = deepcopy(board)
                self.place_Q(n, next_board, num_Q, i)
                self.backtracking(n, next_board, num_Q+1, ret)
                
    def place_Q(self, n, board, y, x):
        i, j = y, x
        while i <= n - 1:
            board[i][j] = '-'
            i += 1
        i, j = y, x
        while i <= n - 1 and j >= 0:
            board[i][j] = '-'
            i += 1
            j -= 1
        i, j = y, x
        while i <= n - 1 and j <= n - 1:
            board[i][j] = '-'
            i += 1
            j += 1
        board[y][x] = 'Q'