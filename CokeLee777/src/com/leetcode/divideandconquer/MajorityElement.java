package com.leetcode.divideandconquer;

import java.util.*;

/**
 * https://leetcode.com/problems/majority-element/
 */
public class MajorityElement {

    public static int mySourceCode(int[] nums) {
        int majorLength = nums.length / 2;
        Map<Integer, Integer> map = new HashMap<>();

        int result = 0;
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
            if(map.get(nums[i]) > majorLength) {
                result = nums[i];
                break;
            }
        }

        return result;
    }

    public static int solution(int[] num) {

        int major=num[0], count = 1;
        for(int i=1; i<num.length;i++){
            if(count==0){
                count++;
                major=num[i];
            }else if(major==num[i]){
                count++;
            }else count--;

        }
        return major;
    }
}
