package com.leetcode.greedy.minnumofsubarray;

import java.util.Stack;

public class MinNumOfSubarray {

    static class MySourceCode{

        public int minNumberOperations(int[] target) {

            // TODO : 첫번째 원소 초기화
            int[] dp = new int[target.length];
            dp[0] = target[0];

            // TODO : Dynamic Programming 수행
            for(int i = 1; i < target.length; i++){
                // 직전의 원소가 0이 아닐경우
                if(target[i-1] != 0){
                    if(target[i] > target[i-1]) dp[i] += dp[i-1] + (target[i] - target[i-1]);
                    else dp[i] = dp[i-1];
                } else {
                    dp[i] += dp[i-1] + target[i];
                }
            }

            return dp[target.length-1];
        }
    }
}