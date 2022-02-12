package com.leetcode.dfsandbfs;

import java.util.HashSet;
import java.util.Set;

/**
 * https://leetcode.com/problems/number-of-provinces/
 */
public class NumberOfProvinces {

    public static class MySourceCode{

        private int[] parent;
        //각 원소의 부모노드 찾기
        private int findParent(int x){
            if(x == parent[x]) return x;
            return parent[x] = findParent(parent[x]);
        }
        //각각의 집합으로 묶기
        private void unionParent(int a, int b){
            a = findParent(a);
            b = findParent(b);

            if(a < b) parent[b] = a;
            else parent[a] = b;
        }

        public int findCircleNum(int[][] isConnected) {
            parent = new int[isConnected.length];

            //자신의 부모를 자기 자신으로 초기화
            for(int i = 0; i < parent.length; i++){
                parent[i] = i;
            }

            //서로소 집합 알고리즘 수행
            for(int i = 0; i < isConnected.length; i++){
                for(int j = 0; j < isConnected[i].length; j++){
                    if(i != j && isConnected[i][j] == 1){
                        unionParent(i, j);
                    }
                }
            }

            Set<Integer> city = new HashSet<>();
            for(int i = 0; i < parent.length; i++){
                city.add(findParent(i));
            }

            return city.size();
        }
    }

    public static class Solution{

        class UnionFind {
            private int count = 0;
            private int[] parent, rank;

            public UnionFind(int n) {
                count = n;
                parent = new int[n];
                rank = new int[n];
                for (int i = 0; i < n; i++) {
                    parent[i] = i;
                }
            }

            public int find(int p) {
                while (p != parent[p]) {
                    parent[p] = parent[parent[p]];    // path compression by halving
                    p = parent[p];
                }
                return p;
            }

            public void union(int p, int q) {
                int rootP = find(p);
                int rootQ = find(q);
                if (rootP == rootQ) return;
                if (rank[rootQ] > rank[rootP]) {
                    parent[rootP] = rootQ;
                }
                else {
                    parent[rootQ] = rootP;
                    if (rank[rootP] == rank[rootQ]) {
                        rank[rootP]++;
                    }
                }
                count--;
            }

            public int count() {
                return count;
            }
        }

        public int findCircleNum(int[][] M) {
            int n = M.length;
            UnionFind uf = new UnionFind(n);
            for (int i = 0; i < n - 1; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (M[i][j] == 1) uf.union(i, j);
                }
            }
            return uf.count();
        }
    }
}
