package com.leetcode.graph.shortestpathcolor;

import java.util.*;

public class ShortestPathWithAlterColors {

    static class MySourceCode{

        class Node implements Comparable<Node>{
            private int index;
            private int distance;
            private char color;

            public Node(int index, int distance, char color) {
                this.index = index;
                this.distance = distance;
                this.color = color;
            }

            public int getIndex() {
                return index;
            }

            public int getDistance() {
                return distance;
            }

            public char getColor() {
                return color;
            }

            @Override
            public int compareTo(Node o) {
                return this.distance - o.distance;
            }
        }

        private List<List<Node>> graph = new ArrayList<>();
        private int[] d;
        private int[][] edgeNums;

        private static final int INF = (int)1e9;

        public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
            //간선개수 배열 초기화
            edgeNums = new int[n][n];
            //그래프 초기화
            initGraph(n, redEdges, blueEdges);
            //최단거리 테이블 초기화
            initShortestTable(n);
            //다익스트라 최단거리 알고리즘 수행
            findShortestPath(0);
            //최단거리 테이블중 가지못하는 곳이 있다면 -1삽입
            for(int i = 0; i < n; i++){
                if(d[i] == INF) d[i] = -1;
            }

            return d;
        }

        private void findShortestPath(int start){
            PriorityQueue<Node> pq = new PriorityQueue<>();
            initStartNode(start, pq);

            //큐가 빌때까지 반복
            while(!pq.isEmpty()){
                Node node = pq.poll();
                int index = node.getIndex();
                int distance = node.getDistance();
                char color = node.getColor();

                //아니면 그래프 탐색
                for(int i = 0; i < graph.get(index).size(); i++){
                    int nextIndex = graph.get(index).get(i).getIndex();
                    char nextColor = graph.get(index).get(i).getColor();
                    //현재 간선의 색깔이랑 같다면 무시
                    if(isSame(color, nextColor))
                        continue;
                    //이미 가본 간선이라면 무시
                    if(edgeNums[index][nextIndex] == 0)
                        continue;
                    //아니라면 거리 비교
                    if(distance + 1 < d[nextIndex]){
                        d[nextIndex] = distance + 1;
                    }

                    pq.offer(new Node(nextIndex, distance + 1, nextColor));
                    edgeNums[index][nextIndex]--;
                }
            }
        }

        private boolean isSame(char color, char nextColor) {
            return color == nextColor;
        }

        private void initStartNode(int start, PriorityQueue<Node> pq) {
            //0에서 0으로가는 간선의 색깔은 존재하지 않으므로 N으로 초기화
            pq.offer(new Node(start, 0, 'N'));
            d[start] = 0;
        }

        private void initShortestTable(int n) {
            d = new int[n];
            Arrays.fill(d, INF);
        }

        private void initGraph(int n, int[][] redEdges, int[][] blueEdges) {

            for(int i = 0; i < n; i++){
                graph.add(new ArrayList<>());
            }
            //그래프 입력받기
            for(int[] redEdge: redEdges){
                graph.get(redEdge[0]).add(new Node(redEdge[1], 1, 'R'));
                edgeNums[redEdge[0]][redEdge[1]]++;
            }
            for (int[] blueEdge : blueEdges) {
                graph.get(blueEdge[0]).add(new Node(blueEdge[1], 1, 'B'));
                edgeNums[blueEdge[0]][blueEdge[1]]++;
            }
        }
    }
}
