package com.leetcode.greedy.maxnumofeatenapples;

import java.util.Comparator;
import java.util.PriorityQueue;

public class MaxNumOfEatenApples {

    static class MySourceCode{

        private PriorityQueue<int[]> appleStorage = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        public int eatenApples(int[] apples, int[] days) {

            int appleCount = 0;
            for(int i = 0; i < apples.length || !appleStorage.isEmpty(); i++){
                //사과가 자라는날 까지 사과를 큐에 삽입
                if(i < apples.length){
                    appleStorage.add(new int[]{i + days[i], apples[i]});
                }
                //현재 가장 날짜가 적게남은 사과가 썩었거나 없는 경우 큐에서 삭제
                while(!appleStorage.isEmpty() && !hasNormalApple(i)){
                    appleStorage.poll();
                }
                //가장 유통기한이 적게남은 사과를 하나먹고 유통기한 하루 빼기
                if(!appleStorage.isEmpty()){
                    appleCount++;
                    appleStorage.peek()[1]--;
                }
            }

            return appleCount;
        }

        private boolean hasNormalApple(int day){
            return appleStorage.peek()[0] > day && appleStorage.peek()[1] > 0;
        }
    }
}
