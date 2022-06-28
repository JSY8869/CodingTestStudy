package com.leetcode.string.satisfiabilityofEE;

public class SatisfiabilityOfEE {

    static class MySourceCode {

        private int[] parent = new int[26];

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

        public boolean equationsPossible(String[] equations) {

            for(int i = 0; i < 26; i++){
                parent[i] = i;
            }

            for (String equation : equations) {
                int a = equation.charAt(0) - 'a';
                int b = equation.charAt(3) - 'a';
                boolean isEquals = (equation.charAt(1) == '=');

                if(isEquals) unionParent(a, b);
            }

            for (String equation : equations) {
                int a = equation.charAt(0) - 'a';
                int b = equation.charAt(3) - 'a';
                boolean isNotEquals = (equation.charAt(1) == '!');

                if(isNotEquals){
                    if(findParent(a) == findParent(b)) return false;
                }
            }

            return true;
        }
    }
}
