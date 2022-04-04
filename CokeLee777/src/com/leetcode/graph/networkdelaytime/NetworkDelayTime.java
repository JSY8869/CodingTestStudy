package com.leetcode.graph.networkdelaytime;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/**
 * https://leetcode.com/problems/network-delay-time/
 */
public class NetworkDelayTime {

    public static class MySourceCode{

        class Node implements Comparable<Node>{

            private int index;
            private int distance;

            public Node(int index, int distance) {
                this.index = index;
                this.distance = distance;
            }

            public int getIndex() {
                return index;
            }

            public int getDistance() {
                return distance;
            }

            @Override
            public int compareTo(Node o) {
                return this.distance - o.distance;
            }
        }

        private List<List<Node>> graph = new ArrayList<>();
        private int[] d;

        private static final int INF = (int)1e9;

        public void dyikstra(int start){
            PriorityQueue<Node> pq = new PriorityQueue<>();
            //자기자신으로 가는 거리 0으로 초기화 후 큐에 삽입
            pq.offer(new Node(start, 0));
            d[start] = 0;

            //큐가 빌때까지 반복
            while(!pq.isEmpty()){
                Node node = pq.poll();
                int index = node.getIndex();
                int distance = node.getDistance();

                //이미 처리된 노드라면 무시
                if(d[index] < distance) continue;

                for(int i = 0; i < graph.get(index).size(); i++){
                    //k에서 index를 거쳐서 i로 가는 경우가 k에서 i로 바로가는 경우보다 짧다면 최단거리 변경
                    int cost = d[index] + graph.get(index).get(i).getDistance();
                    if(cost < d[graph.get(index).get(i).getIndex()]){
                        d[graph.get(index).get(i).getIndex()] = cost;
                        pq.offer(new Node(graph.get(index).get(i).getIndex(), cost));
                    }
                }
            }
        }

        public int networkDelayTime(int[][] times, int n, int k) {
            //그래프 초기화
            for(int i = 0; i <= n; i++)
                graph.add(new ArrayList<>());

            for(int i = 0; i < times.length; i++){
                int start = times[i][0];
                int end = times[i][1];
                int distance = times[i][2];
                //단방향 그래프
                graph.get(start).add(new Node(end, distance));
            }

            //최단거리 테이블 초기화
            d = new int[n+1];
            Arrays.fill(d, INF);

            //다익스트라 최단거리 알고리즘 수행
            dyikstra(k);

            int finishTime = 0;
            for(int i = 1; i <= n; i++){
                //신호가 도달할 수 없는곳이 존재한다면 -1반환
                if(isNotConnected(i)) return -1;
                //아니면 비교
                finishTime = Math.max(d[i], finishTime);
            }

            return finishTime;
        }

        private boolean isNotConnected(int i) {
            return d[i] == INF;
        }
    }
}
