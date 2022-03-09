package com.leetcode.dfsandbfs;

import java.util.LinkedList;
import java.util.Queue;

/**
 * https://leetcode.com/problems/shortest-bridge/
 */
public class ShortestBridge {

    public static class MySourceCode{

        private final int[] dx = {0,0,1,-1};
        private final int[] dy = {1,-1,0,0};
        private int islandNum = 1;

        public int shortestBridge(int[][] grid) {
            Queue<int[]> queue = new LinkedList<>();
            int[][] bridge = new int[grid.length][grid[0].length];          //최단거리 테이블
            boolean[][] visited = new boolean[grid.length][grid[0].length]; //방문처리 배열

            //dfs로 섬의 번호 매기기
            for(int i = 0; i < grid.length; i++){
                for(int j = 0; j < grid[i].length; j++){
                    if(grid[i][j] == 1 && !visited[i][j]){
                        dfs(grid, visited, i, j, queue);
                        islandNum++;
                    }
                }
            }

            //bfs로 1번섬과 2번섬과의 최단거리 측정
            int min = Integer.MAX_VALUE;
            while(!queue.isEmpty()){
                int[] now = queue.poll();

                for(int i = 0; i < 4; i++){
                    int nx = now[0] + dx[i];
                    int ny = now[1] + dy[i];

                    if(nx < 0 || nx >= grid.length || ny < 0 || ny >= grid[0].length)
                        continue;
                    //섬이 아니라면 다리를 세운다
                    if(grid[nx][ny] != 1 && grid[nx][ny] != 2){
                        //이미 세워진 다리라면 지금 경로의 최단거리와 비교
                        if(bridge[nx][ny] != 0){
                            bridge[nx][ny] = Math.min(bridge[nx][ny], bridge[now[0]][now[1]] + 1);
                        }//처음 세운 다리라면 지금 거리 + 1을 넣고 큐에 삽입
                        else {
                            queue.offer(new int[]{nx, ny});
                            bridge[nx][ny] = bridge[now[0]][now[1]] + 1;
                        }
                    }//또다른 섬이라면 모든 경로로부터 최단거리 비교
                    else if(grid[nx][ny] == 2){
                        min = Math.min(min, bridge[now[0]][now[1]]);
                    }
                }
            }

            return min;
        }

        private void dfs(int[][] grid, boolean[][] visited, int x, int y, Queue<int[]> queue){
            //방문처리와 섬번호 처리
            visited[x][y] = true;
            grid[x][y] = islandNum;
            //섬번호가 1인 것만 큐에 삽입
            if(islandNum == 1) queue.offer(new int[]{x, y});

            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 0 || nx >= grid.length || ny < 0 || ny >= grid[0].length)
                    continue;
                if(grid[nx][ny] == 1 && !visited[nx][ny]){
                    dfs(grid, visited, nx, ny, queue);
                }
            }
        }
    }

    public static class Solution{

        public int shortestBridge(int[][] A) {
            int m = A.length, n = A[0].length;
            boolean[][] visited = new boolean[m][n];
            int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            Queue<int[]> q = new LinkedList<>();
            boolean found = false;
            // 1. dfs to find an island, mark it in `visited`
            for (int i = 0; i < m; i++) {
                if (found) {
                    break;
                }
                for (int j = 0; j < n; j++) {
                    if (A[i][j] == 1) {
                        dfs(A, visited, q, i, j, dirs);
                        found = true;
                        break;
                    }
                }
            }
            // 2. bfs to expand this island
            int step = 0;
            while (!q.isEmpty()) {
                int size = q.size();
                while (size-- > 0) {
                    int[] cur = q.poll();
                    for (int[] dir : dirs) {
                        int i = cur[0] + dir[0];
                        int j = cur[1] + dir[1];
                        if (i >= 0 && j >= 0 && i < m && j < n && !visited[i][j]) {
                            if (A[i][j] == 1) {
                                return step;
                            }
                            q.offer(new int[]{i, j});
                            visited[i][j] = true;
                        }
                    }
                }
                step++;
            }
            return -1;
        }
        private void dfs(int[][] A, boolean[][] visited, Queue<int[]> q, int i, int j, int[][] dirs) {
            if (i < 0 || j < 0 || i >= A.length || j >= A[0].length || visited[i][j] || A[i][j] == 0) {
                return;
            }
            visited[i][j] = true;
            q.offer(new int[]{i, j});
            for (int[] dir : dirs) {
                dfs(A, visited, q, i + dir[0], j + dir[1], dirs);
            }
        }
    }
}
