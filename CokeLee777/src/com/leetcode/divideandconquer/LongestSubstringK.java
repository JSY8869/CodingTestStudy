package com.leetcode.divideandconquer;

import java.util.Arrays;

/**
 * https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
 */
public class LongestSubstringK {

    public static class Solution{

        public int longestSubstring(String s, int k) {
            char[] str = s.toCharArray();
            return helper(str,0,s.length(),k);
        }

        private int helper(char[] str, int start, int end,  int k){
            //남은 문자열의 개수가 k보다 작다면
            if (end - start < k) return 0;
            //현재 부분의 각각의 알파벳 개수 더하기
            int[] nums = new int[26];
            for (int i = start; i<end; i++) {
                int idx = str[i] - 'a';
                nums[idx]++;
            }
            for (int i=0; i<26; i++) {
                //현재 문자의 개수가 k보다 작다면
                if (nums[i] < k && nums[i] > 0) {
                    for (int j = start; j<end; j++) {
                        //j번째 알파벳의 개수가 k보다 적다면 분할
                        if (str[j] == i+'a') {
                            int left = helper(str, start, j, k);
                            int right = helper(str, j+1, end, k);
                            //분할된 왼쪽과 오른쪽 부분에 대해서 비교
                            return Math.max(left, right);
                        }
                    }
                }
            }
            //현재 문자열의 모든 알파벳이 k보다 크다면 전체 문자열의 길이 반환
            return end - start;
        }
    }
}
