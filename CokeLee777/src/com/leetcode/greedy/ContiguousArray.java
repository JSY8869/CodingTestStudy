package com.leetcode.greedy;

import java.util.HashMap;
import java.util.Map;

/**
 * https://leetcode.com/problems/contiguous-array/
 */
public class ContiguousArray {

    public static class Solution{

        public int findMaxLength(int[] nums) {
            // 배열안의 0인 원소들 -1로 초기화
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] == 0) nums[i] = -1;
            }
            // Key: sum, Value: index
            Map<Integer, Integer> sumToIndex = new HashMap<>();
            /**
             * ====== Key Point ======
             * index: -1 의 합을 0으로 초기화 -> 첫번째 인덱스부터의 길이를 비교하기 위함
             */
            sumToIndex.put(0, -1);

            int sum = 0, max = 0;
            for (int i = 0; i < nums.length; i++) {
                //현재값 더하기
                sum += nums[i];
                //현재 인덱스까지의 합과 동일한 값이 존재한다면 최대길이 비교
                if (sumToIndex.containsKey(sum)) {
                    max = Math.max(max, i - sumToIndex.get(sum));
                }
                //아니라면 현재 인덱스까지의 합 map 에 삽입
                else {
                    sumToIndex.put(sum, i);
                }
            }

            return max;
        }
    }

}
