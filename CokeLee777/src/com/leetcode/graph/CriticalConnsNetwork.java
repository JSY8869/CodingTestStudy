package com.leetcode.graph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * https://leetcode.com/problems/critical-connections-in-a-network/
 */
public class CriticalConnsNetwork {

    public static class Solution{

        private List<List<Integer>> edges = new ArrayList<>();
        private List<List<Integer>> results = new ArrayList<>();
        private boolean[] visited;
        private int[] timeStampAtThatNode, timer;

        public void criticalConnectionsUtil(int parent, int node){
            //현재 노드 방문처리
            visited[node] = true;
            timeStampAtThatNode[node] = timer[0]++;
            int currentTimeStamp = timeStampAtThatNode[node];

            for(int oneNeighbour: edges.get(node)){
                //한 이웃노드가 부모라면 무시
                if(oneNeighbour == parent) continue;
                //방문하지 않은 이웃노드가 있다면 방문
                if(!visited[oneNeighbour]) criticalConnectionsUtil(node, oneNeighbour);
                //타임스탬프가 더 작은값 부여
                timeStampAtThatNode[node] = Math.min(timeStampAtThatNode[node], timeStampAtThatNode[oneNeighbour]);
                //한 이웃과 그룹이름이 다르다면 결과값 삽입
                if(currentTimeStamp < timeStampAtThatNode[oneNeighbour]) results.add(Arrays.asList(node, oneNeighbour));
            }
        }

        public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
            //그래프 초기화
            for(int i = 0; i < n; i++){
                edges.add(new ArrayList<>());
            }

            for(int i = 0; i < connections.size(); i++){
                int a = connections.get(i).get(0);
                int b = connections.get(i).get(1);
                //양방향 이동 가능 a -> b, b -> a
                edges.get(a).add(b);
                edges.get(b).add(a);
            }

            //배열 초기화
            visited = new boolean[n];
            timeStampAtThatNode = new int[n];
            timer = new int[1];

            criticalConnectionsUtil(-1, 0);

            return results;
        }
    }
}
