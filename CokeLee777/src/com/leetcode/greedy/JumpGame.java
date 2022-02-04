package com.leetcode.greedy;

/**
 * https://leetcode.com/problems/jump-game/
 */
public class JumpGame {

    public boolean mySourceCode(int[] nums) {
        int nowIdx = 0, lastIdx = nums.length-1;
        boolean[] canStay = new boolean[nums.length];
        //시작위치 방문처리
        canStay[0] = true;

        while(nowIdx <= lastIdx){
            if(!canStay[nowIdx]){
                nowIdx++;
                continue;
            }

            for(int i = nowIdx; i <= nowIdx + nums[nowIdx]; i++){
                if(i >= nums.length) break;
                canStay[i] = true;
            }

            nowIdx++;
        }

        return canStay[lastIdx];
    }

    public boolean solution(int[] A) {
        int max = 0;
        for(int i=0;i<A.length;i++){
            if(i>max) {return false;}
            max = Math.max(A[i]+i,max);
        }
        return true;
    }
}
