package com.leetcode.binarysearch;

import java.util.*;

/**
 * https://leetcode.com/problems/find-the-duplicate-number/
 */
public class FindTheDuplicateNumber {

    public int mySourceCode(int[] nums) {
        int result = 0;
        Arrays.sort(nums);
        Set<Integer> set = new HashSet<>();

        for(int i = 0; i < nums.length; i++){
            if(set.contains(nums[i])) {
                result = nums[i];
                break;
            }
            set.add(nums[i]);
        }

        return result;
    }

    public int solution(int[] nums) {
        int low = 1, high = nums.length - 1;
        while (low <= high) {
            int mid = (int) (low + (high - low) * 0.5);
            int cnt = 0;
            for (int a : nums) {
                if (a <= mid) ++cnt;
            }
            if (cnt <= mid) low = mid + 1;
            else high = mid - 1;
        }
        return low;
    }
}
