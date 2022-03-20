package com.leetcode.dfsandbfs;

import java.util.*;

/**
 * https://leetcode.com/problems/find-all-people-with-secret/
 */
public class FindAllPeopleWithSecret {

    public static class MySourceCode{

        private Set<Integer> knowOfSecret = new HashSet<>();
        private int[] parent;

        public int findParent(int x){
            if(x == parent[x]) return x;
            return parent[x] = findParent(parent[x]);
        }

        public void unionParent(int a, int b){
            a = findParent(a);
            b = findParent(b);

            if(a < b) parent[b] = a;
            else parent[a] = b;
        }

        public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
            //미팅 시간을 빠른 순서대로 정렬
            Arrays.sort(meetings, Comparator.comparingInt(m -> m[2]));

            //0번 사람과 첫번째사람 결과값에 삽입
            knowOfSecret.add(0);
            knowOfSecret.add(firstPerson);

            //부모 테이블 초기화
            parent = new int[n];
            for(int i = 0; i < n; i++){
                parent[i] = i;
            }

            unionParent(0, firstPerson);

            //시간순서대로 미팅 진행
            //같은 시간에 여러개의 미팅이 있을 경우 비밀을 알고있는 사람부터 미팅 진행
            int prevTime = 0;
            Queue<Integer> tmp = new LinkedList<>();
            for(int i = 0; i < meetings.length; i++){
                int person1 = meetings[i][0];
                int person2 = meetings[i][1];
                int time = meetings[i][2];

                //전 시간과 같은시간이 아니라면
                while(!tmp.isEmpty() && time != prevTime){
                    Integer now = tmp.poll();

                    //비밀을 알지 못한다면 리셋
                    if(findParent(now) != 0){
                        parent[now] = now;
                        continue;
                    }
                    //비밀을 안다면
                    knowOfSecret.add(now);
                }

                //두 사람 서로소 알고리즘 수행
                unionParent(person1, person2);
                tmp.add(person1); tmp.add(person2);

                prevTime = time;
            }

            //남은 사람들 처리
            while(!tmp.isEmpty()){
                Integer now = tmp.poll();

                //비밀을 알지 못한다면 리셋
                if(findParent(now) != 0){
                    parent[now] = now;
                    continue;
                }
                //비밀을 안다면
                knowOfSecret.add(now);
            }

            return new ArrayList<>(knowOfSecret);
        }
    }
}