package com.leetcode.greedy.maxareaofcake;

import java.util.Arrays;

public class MaxAreaOfPieceOfCake {

    static class MySourceCode{

        private static final int INF = (int)1e9;

        public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
            Arrays.sort(horizontalCuts);
            Arrays.sort(verticalCuts);

            return (int)(getMaxLength(horizontalCuts, h) * getMaxLength(verticalCuts, w) % (INF + 7)) ;
        }

        private long getMaxLength(int[] cutArr, int len){

            long maxLen = cutArr[0];
            for(int i = 1; i < cutArr.length; i++){
                maxLen = Math.max(maxLen, cutArr[i] - cutArr[i-1]);
            }

            return Math.max(maxLen, len - cutArr[cutArr.length-1]);
        }
    }
}
