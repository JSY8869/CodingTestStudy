package com.leetcode.simulation.carpooling;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Carpooling {

    static class MySourceCode{

        public boolean carPooling(int[][] trips, int capacity) {
            //각각의 여행객들의 출발날짜를 기준으로 오름차순 정렬
            Arrays.sort(trips, Comparator.comparingInt(t -> t[1]));
            //여행하고있는 여행객들의 정보를 담을 큐 생성 -> 여행이 끝나는 시점을 기준으로 오름차순 정렬
            PriorityQueue<int[]> triping = new PriorityQueue<>(Comparator.comparingInt(o -> o[2]));
            for(int i = 0; i < trips.length; i++){
                int passengers = trips[i][0];
                int startDay = trips[i][1];
                //타고있는 여행객들이 내린다면
                while(!triping.isEmpty() && triping.peek()[2] <= startDay){
                    //내린만큼 남은좌석 추가
                    capacity += triping.poll()[0];
                }
                //다음 여행객들이 차에 탈 수 없다면
                if(noMoreSeats(trips[i], capacity)) return false;
                //탈수 있다면
                triping.add(trips[i]);
                capacity -= passengers;
            }
            return true;
        }

        private boolean noMoreSeats(int[] trip, int capacity) {
            return trip[0] > capacity;
        }
    }
}
