package com.leetcode.simulation.spiralmatrix;

import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/spiral-matrix/
 */
public class SpiralMatrix {

    public static class MySourceCode{

        private final int[] dx = {0,1,0,-1};
        private final int[] dy = {1,0,-1,0};

        private List<Integer> ans = new ArrayList<>();
        private boolean[][] visited;
        private int row, col;

        public void moveSpiralOrder(int[][] matrix, int dir){
            //현재 방향으로 직진
            int x = 0, y = 0;
            while(canMove(x, y)){
                //움직일 수 있으면 결과값 삽입 후 방문처리
                ans.add(matrix[x][y]);
                visited[x][y] = true;
                //이동해야할 곳이 범위를 벗어났다면 회전
                if(!canMove(x + dx[dir], y + dy[dir])){
                    dir = turnClockwise(dir);
                }
                //한칸 앞으로 이동
                x += dx[dir];
                y += dy[dir];
            }
        }

        private int turnClockwise(int dir) {
            return dir + 1 == 4 ? 0 : dir + 1;
        }

        private boolean canMove(int x, int y) {
            return x >= 0 && x < row && y >= 0 && y < col && !visited[x][y];
        }

        public List<Integer> spiralOrder(int[][] matrix) {
            //배열의 행, 열의 길이
            row = matrix.length;
            col = matrix[0].length;
            //방문처리 배열 초기화
            visited = new boolean[row][col];

            //시뮬레이션 시작
            moveSpiralOrder(matrix, 0);

            return ans;
        }

        public static void main(String[] args) {
            MySourceCode T = new MySourceCode();
            int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
            T.spiralOrder(matrix);
        }
    }
}
