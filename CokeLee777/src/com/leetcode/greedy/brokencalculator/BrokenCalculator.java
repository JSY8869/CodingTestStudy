package com.leetcode.greedy.brokencalculator;

/**
 * https://leetcode.com/problems/broken-calculator/
 */
public class BrokenCalculator {

    public static class MySourceCode{

        public int brokenCalc(int startValue, int target) {
            //타겟에 도달했다면 0 반환
            if(startValue == target) return 0;
                //타겟에 도달하지 못했다면
            else if (startValue < target){
                //2로 나누어진다면 나누는 연산 수행
                if(target % 2 == 0) return brokenCalc(startValue, target / 2) + 1;
                //아니면 1을 더하는 연산 수행
                else return brokenCalc(startValue, target + 1) + 1;
            } else {
                //시작값이 타겟보다 커진다면 -1연산밖에 못하므로 둘의 차이 반환
                return startValue - target;
            }
        }
    }

    public static class Solution{

        public int brokenCalc(int startValue, int target) {
            if(startValue >= target) return startValue - target;
            if(target % 2 == 0){
                return 1 + brokenCalc(startValue, target / 2);
            }
            return 1 + brokenCalc(startValue, target + 1);
        }
    }
}
