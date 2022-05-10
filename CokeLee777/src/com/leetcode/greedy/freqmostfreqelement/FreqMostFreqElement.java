package com.leetcode.greedy.freqmostfreqelement;

import java.util.Arrays;

public class FreqMostFreqElement {

    static class MySourceCode{
        //방법 1
        public int maxFrequency(int[] nums, int k) {
            //오름차순으로 배열 정렬
            Arrays.sort(nums);

            //같은값에 도달할 수 있는 최대 개수 구하기
            int max = 1;
            int leftOperation = k;
            for(int right = nums.length-1, left = right-1; right > 0; right--){
                //제일 큰 숫자가 바뀌었으므로 그 숫자를 기준으로 모두 연산횟수 갱신
                if(leftOperation != k){
                    leftOperation += ((right-left) * (nums[right+1] - nums[right]));
                }
                //남은 연산횟수로 같은 숫자로 만들수있는 숫자가 있으면
                while(left >= 0 && nums[left] + leftOperation >= nums[right]){
                    leftOperation -= (nums[right] - nums[left]);
                    left--;
                }
                //최대값 갱신
                max = Math.max(right - left, max);
            }

            return max;
        }

        //시간초과 O(NlogN)
        public int maxFrequency2(int[] nums, int k) {
            //오름차순으로 배열 정렬
            Arrays.sort(nums);

            //같은값에 도달할 수 있는 최대 개수 구하기
            int max = 1;
            for(int right = nums.length-1; right > 0; right--){
                int leftOperation = k;
                int left = right-1;
                while(left >= 0 && nums[left] + leftOperation >= nums[right]){
                    leftOperation -= (nums[right] - nums[left]);
                    left--;
                }
                max = Math.max(right - left, max);
            }

            return max;
        }
    }
}
