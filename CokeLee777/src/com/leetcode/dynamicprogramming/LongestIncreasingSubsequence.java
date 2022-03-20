package com.leetcode.dynamicprogramming;

/**
 * https://leetcode.com/problems/longest-increasing-subsequence/
 */
public class LongestIncreasingSubsequence {

    public static class MySourceCode{

        public int lengthOfLIS(int[] nums) {
            int[] dp = new int[nums.length];

            int max = 0;
            for(int i = 0; i < nums.length; i++){
                dp[i] = 1;

                //0~i까지 탐색
                for(int j = 0; j < i; j++){
                    //j번째 원소가 i번째 원소보다 작으면서 i번째 dp가 j번째 dp + 1보다 작은경우
                    if(nums[j] < nums[i] && dp[i] < dp[j] + 1){
                        dp[i] = dp[j] + 1;
                    }
                }
                //최대값 갱신
                max = Math.max(dp[i], max);
            }

            return max;
        }
    }
}
