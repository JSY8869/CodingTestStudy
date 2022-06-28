package com.leetcode.greedy.pizzaWith3nSlices;

public class PizzaWith3nSlices {

    static class MySourceCode {

        private int getMaxPizza(int[] slices, int start, int end, int canTakeSlices){
            int slicesSize = end - start;
            int dpRows = slicesSize + 1;
            int dpCols = canTakeSlices + 1;
            int[][] dp = new int[dpRows][dpCols];

            for(int i = 1; i < dpRows; i++){
                for(int j = 1; j < dpCols; j++){
                    int slicesIndex = (i + start) - 1;
                    if(i == 1){
                        dp[i][j] = slices[slicesIndex];
                    } else {
                        int notTakingSlice = dp[i-1][j];
                        int takingSlice = slices[slicesIndex] + dp[i-2][j-1];
                        dp[i][j] = Math.max(notTakingSlice, takingSlice);
                    }
                }
            }

            return dp[slicesSize][canTakeSlices];
        }

        public int maxSizeSlices(int[] slices) {
            int n = slices.length;
            int canTakeSlices = n / 3;
            int takeFirstSlice = getMaxPizza(slices, 0, n-1, canTakeSlices);
            int takeLastSlice = getMaxPizza(slices, 1, n, canTakeSlices);

            return Math.max(takeFirstSlice, takeLastSlice);
        }
    }
}
