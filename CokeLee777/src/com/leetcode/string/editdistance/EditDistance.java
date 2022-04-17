package com.leetcode.string.editdistance;


public class EditDistance {

    static class Solution{

        public int minDistance(String word1, String word2) {

            if(word1.length() == 0){
                return word2.length();
            }
            if(word2.length() == 0){
                return word1.length();
            }
            //현재 인덱스에서 두 문자가 같다면 다음 인덱스 비교
            if(word1.charAt(0) == word2.charAt(0)){
                return minDistance(word1.substring(1),word2.substring(1));
            } else {
                //insert 연산
                int insert = minDistance(word1,word2.substring(1));
                //delete 연산
                int delete = minDistance(word1.substring(1),word2);
                //replace 연산
                int replace = minDistance(word1.substring(1),word2.substring(1));

                //세개의 연산 중에 가장 연산횟수가 짧은 것 반환
                return 1 + Math.min(insert,Math.min(delete,replace));
            }
        }
    }

    static class Solution2{

        public int minDistance(String word1, String word2) {
            int m = word1.length();
            int n = word2.length();

            int[][] cost = new int[m + 1][n + 1];
            for(int i = 0; i <= m; i++)
                cost[i][0] = i;
            for(int i = 1; i <= n; i++)
                cost[0][i] = i;

            for(int i = 0; i < m; i++) {
                for(int j = 0; j < n; j++) {
                    if(word1.charAt(i) == word2.charAt(j))
                        cost[i + 1][j + 1] = cost[i][j];
                    else {
                        int a = cost[i][j];
                        int b = cost[i][j + 1];
                        int c = cost[i + 1][j];
                        cost[i + 1][j + 1] = a < b ? (Math.min(a, c)) : (Math.min(b, c));
                        cost[i + 1][j + 1]++;
                    }
                }
            }
            return cost[m][n];
        }
    }
}
