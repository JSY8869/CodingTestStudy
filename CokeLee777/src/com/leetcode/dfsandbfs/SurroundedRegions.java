package com.leetcode.dfsandbfs;

/**
 * https://leetcode.com/problems/surrounded-regions/
 */
public class SurroundedRegions {

    public static int[] dx = {0,0,1,-1};
    public static int[] dy = {1,-1,0,0};
    public static boolean isCaptured = true;

    public static void copyDfs(int x, int y, char[][] board){
        board[x][y] = '*';
        //네 방향 모두 반복
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            //네 방향중 벽이라면
            if(nx < 0 || nx >= board.length || ny < 0 || ny >= board[0].length){
                isCaptured = false;
                continue;
            }
            //'O'를 만나면 전진
            if(board[nx][ny] == 'O'){
                copyDfs(nx, ny, board);
            }
        }
    }

    public static void dfs(int x, int y, char[][] board, boolean[][] visited){
        visited[x][y] = true;
        board[x][y] = 'X';
        //네 방향 모두 반복
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            //'O'를 만나면 전진
            if(board[nx][ny] == 'O' && !visited[nx][ny]){
                dfs(nx, ny, board, visited);
            }
        }
    }

    public static void mySourceCode(char[][] board) {
        //행, 열의 길이
        int m = board.length, n = board[0].length;
        //방문처리 배열
        boolean[][] visited = new boolean[m][n];
        //보드 복사
        char[][] copyBoard = new char[m][n];
        for(int i = 0; i < copyBoard.length; i++){
            System.arraycopy(board[i], 0, copyBoard[i], 0, board[0].length);
        }

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(copyBoard[i][j] == 'O'){
                    isCaptured = true;
                    copyDfs(i, j, copyBoard);
                    //네 방향으로 둘러쌓였다면
                    if(isCaptured){
                        dfs(i, j, board, visited);
                    }
                }
            }
        }

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    /**
     * 정답 코드
     */
    public void solution(char[][] board) {
        if (board.length == 0 || board[0].length == 0)
            return;
        if (board.length < 2 || board[0].length < 2)
            return;
        int m = board.length, n = board[0].length;
        //Any 'O' connected to a boundary can't be turned to 'X', so ...
        //Start from first and last column, turn 'O' to '*'.
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O')
                boundaryDFS(board, i, 0);
            if (board[i][n-1] == 'O')
                boundaryDFS(board, i, n-1);
        }
        //Start from first and last row, turn '0' to '*'
        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O')
                boundaryDFS(board, 0, j);
            if (board[m-1][j] == 'O')
                boundaryDFS(board, m-1, j);
        }
        //post-prcessing, turn 'O' to 'X', '*' back to 'O', keep 'X' intact.
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                else if (board[i][j] == '*')
                    board[i][j] = 'O';
            }
        }
    }
    //Use DFS algo to turn internal however boundary-connected 'O' to '*';
    private void boundaryDFS(char[][] board, int i, int j) {
        if (i < 0 || i > board.length - 1 || j <0 || j > board[0].length - 1)
            return;
        if (board[i][j] == 'O')
            board[i][j] = '*';
        if (i > 1 && board[i-1][j] == 'O')
            boundaryDFS(board, i-1, j);
        if (i < board.length - 2 && board[i+1][j] == 'O')
            boundaryDFS(board, i+1, j);
        if (j > 1 && board[i][j-1] == 'O')
            boundaryDFS(board, i, j-1);
        if (j < board[i].length - 2 && board[i][j+1] == 'O' )
            boundaryDFS(board, i, j+1);
    }
}
