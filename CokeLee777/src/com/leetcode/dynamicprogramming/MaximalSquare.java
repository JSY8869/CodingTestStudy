package com.leetcode.dynamicprogramming;

/**
 * https://leetcode.com/problems/maximal-square/
 */
public class MaximalSquare {

    public static class MySourceCode{

        public int maximalSquare(char[][] matrix) {
            //그래프의 행, 열
            int row = matrix.length, col = matrix[0].length;
            //dp를 계산하기 위해서 인덱스 + 1 까지 잡음
            int[][] dp = new int[row+1][col+1];

            int max = 0;
            for(int i = 0; i < row; i++){
                for(int j = 0; j < col; j++){
                    if(matrix[i][j] == '1'){
                        dp[i+1][j+1] = Math.min(Math.min(dp[i][j+1], dp[i+1][j]), dp[i][j]) + 1;
                        max = Math.max(max, dp[i+1][j+1]);
                    }
                }
            }
            //사각형의 넓이를 리턴
            return max * max;
        }
    }
}
