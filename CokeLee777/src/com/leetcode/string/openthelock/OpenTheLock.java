package com.leetcode.string.openthelock;

import java.util.*;
import java.util.stream.Collectors;

/**
 * https://leetcode.com/problems/open-the-lock/
 */
public class OpenTheLock {

    public static class MySourceCode{

        private static Set<String> deads = new HashSet<>();
        private static Set<String> visited = new HashSet<>();

        public int openLock(String[] deadends, String target) {
            Queue<String> queue = new LinkedList<>();
            deads = Arrays.stream(deadends)
                    .collect(Collectors.toSet());
            visited = new HashSet<>();
            //시작위치 방문처리 및 큐에 삽입
            queue.offer("0000");
            visited.add("0000");

            //큐가 빌때까지 반복
            int step = 0;
            while(!queue.isEmpty()){
                //현재 번호에서 다음으로 가는 방법을 센다
                int size = queue.size();
                while(size-- > 0){
                    String now = queue.poll();
                    //deadends라면 무시
                    if(isDeadends(now)){
                        size--;
                        continue;
                    }
                    //아니라면 타겟이랑 비교
                    if(isTarget(target, now)) return step;
                    //현재 비밀번호에서 갈 수 있는 비밀번호 찾기
                    findPossibleWayFromNow(queue, now);
                }
                step++;
            }
            //비밀번호를 맞출수있는 방법이 없다면 -1출력
            return -1;
        }

        private void findPossibleWayFromNow(Queue<String> queue, String now) {
            //네 번호 모두 반복하면서 가능한 번호 삽입
            StringBuilder tmp = new StringBuilder(now);
            for(int i = 0; i < 4; i++){
                //i번째 위치에서 번호
                char x = tmp.charAt(i);
                //i번째 비밀번호만 1증가, 1감소
                String s1 = tmp.substring(0, i) + (x == '9' ? 0 : x - '0' + 1) + tmp.substring(i + 1);
                String s2 = tmp.substring(0, i) + (x == '0' ? 9 : x - '0' - 1) + tmp.substring(i + 1);
                //s1, s2가 방문하지 않았고, deadends가 아니면 큐에 삽입
                if(isNotVisited(s1) && !isDeadends(s1)){
                    queue.offer(s1);
                    visited.add(s1);
                }
                if(isNotVisited(s2) && !isDeadends(s2)){
                    queue.offer(s2);
                    visited.add(s2);
                }
            }
        }

        private boolean isNotVisited(String s1) {
            return !visited.contains(s1);
        }

        private boolean isDeadends(String now) {
            return deads.contains(now);
        }

        private boolean isTarget(String target, String now) {
            return now.equals(target);
        }
    }
}
