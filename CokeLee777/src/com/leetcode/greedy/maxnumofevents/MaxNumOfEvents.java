package com.leetcode.greedy.maxnumofevents;

import java.util.*;

public class MaxNumOfEvents {

    static class MySourceCode{

        private PriorityQueue<Integer> eventQueue = new PriorityQueue<>();

        public int maxEvents(int[][] events) {
            // TODO : 이벤트 시작일을 기준으로 오름차순 정렬
            Arrays.sort(events, Comparator.comparingInt(e -> e[0]));

            int attendCount = 0;
            for(int day = 1, eventIdx = 0; day <= 100000; day++){
                deleteExpiredEvents(day);
                eventIdx = enqueStartEvents(events, day, eventIdx);
                // TODO : 오늘 참가할 수 있는 이벤트가 있다면 참가
                if(!eventQueue.isEmpty()){
                    eventQueue.poll();
                    attendCount++;
                }
            }

            return attendCount;
        }

        // TODO : 오늘 시작하는 이벤트가 있다면 모두 큐에 삽입(끝나는 날을 삽입)
        private int enqueStartEvents(int[][] events, int day, int eventIdx) {
            while(eventIdx < events.length && events[eventIdx][0] == day)
                eventQueue.offer(events[eventIdx++][1]);
            return eventIdx;
        }

        // TODO : 날짜가 지난 이벤트를 버린다
        private void deleteExpiredEvents(int day) {
            while(!eventQueue.isEmpty() && eventQueue.peek() < day)
                eventQueue.poll();
        }

        //시간초과
        public int maxEvents2(int[][] events) {

            Arrays.sort(events, (o1, o2) -> {
                if(o1[1] != o2[1]) return o1[1] - o2[1];
                else return o1[0] - o2[0];
            });

            int attendCount = 0;
            Set<Integer> visited = new HashSet<>();
            for(int[] event: events){
                int startDay = event[0];
                int endDay = event[1];

                while(startDay <= endDay){
                    if(!visited.contains(startDay)){
                        attendCount++;
                        visited.add(startDay);
                        break;
                    }
                    startDay++;
                }
            }

            return attendCount;
        }
    }
}
