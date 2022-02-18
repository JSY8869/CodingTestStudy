package com.leetcode.backtracking;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * https://leetcode.com/problems/n-queens/
 */
public class NQueens {

    public static class Solution{

        public List<List<String>> solveNQueens(int n) {
            //n*n의 체스판 생성 후 '.'으로 초기화
            char[][] board = new char[n][n];
            for(int i = 0; i < n; i++)
                for(int j = 0; j < n; j++)
                    board[i][j] = '.';
            List<List<String>> res = new ArrayList<>();
            dfs(board, 0, res);
            return res;
        }

        private void dfs(char[][] board, int colIndex, List<List<String>> res) {
            //모든 열을 다 돌았다면 결과값에 삽입 후 메서드 종료
            if(colIndex == board.length) {
                res.add(construct(board));
                return;
            }

            for(int i = 0; i < board.length; i++) {
                //퀸이 만나는지 안만나는지 판단
                if(validate(board, i, colIndex)) {
                    board[i][colIndex] = 'Q';
                    dfs(board, colIndex + 1, res);
                    board[i][colIndex] = '.';
                }
            }
        }

        private boolean validate(char[][] board, int x, int y) {
            for(int i = 0; i < board.length; i++) {
                for(int j = 0; j < y; j++) {
                    /**
                     * (x + j == y + i) : ('\')왼쪽으로 기울어진 대각선 방향으로 퀸이 만날경우
                     * (x + y == i + j) : ('/')오른쪽으로 기울어진 대각선 방향으로 퀸이 만날경우
                     * (x == i) : 퀸들이 같은 행에 속한다면
                     */
                    if(board[i][j] == 'Q' && (x + j == y + i || x + y == i + j || x == i))
                        return false;
                }
            }
            return true;
        }

        private List<String> construct(char[][] board) {
            List<String> res = new LinkedList<>();
            for(int i = 0; i < board.length; i++) {
                String s = new String(board[i]);
                res.add(s);
            }
            return res;
        }
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        T.solveNQueens(4);
    }
}
