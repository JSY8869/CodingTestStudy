package com.leetcode.graph.keyandrooms;

import java.util.*;

public class KeyAndRooms {

    static class MySourceCode{

        private boolean[] visited;

        public boolean canVisitAllRooms(List<List<Integer>> rooms) {
            visited = new boolean[rooms.size()];

            return bfs(0, rooms);
        }

        private boolean bfs(int start, List<List<Integer>> roomKeys){
            Queue<Integer> keyStore = new LinkedList<>();
            keyStore.offer(start);
            visited[start] = true;

            int enteredRoom = 0;
            while(!keyStore.isEmpty()){
                Integer roomNumber = keyStore.poll();
                enteredRoom++;
                // TODO : 현재 방에 존재하는 열쇠중에 방문하지 않은 방의 열쇠가 있다면 넣기
                for (Integer key : roomKeys.get(roomNumber)) {
                    if(!visited[key]) {
                        keyStore.offer(key);
                        visited[key] = true;
                    }
                }
            }

            return enteredRoom == roomKeys.size();
        }
    }
}
