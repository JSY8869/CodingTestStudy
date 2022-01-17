package com.leetcode.greedy;

import java.util.PriorityQueue;

/**
 * https://leetcode.com/problems/reorganize-string/
 */
public class ReorganizeString {
    
    public static class Alphabet implements Comparable<Alphabet>{
        private char value;
        private int count;

        public Alphabet(char value, int count) {
            this.value = value;
            this.count = count;
        }

        public char getValue() {
            return value;
        }

        public int getCount() {
            return count;
        }

        public void minusCount() {
            this.count--;
        }

        @Override
        public int compareTo(Alphabet alphabet) {
            if(this.count > alphabet.count) return -1;
            else return 1;
        }
    }

    public static String mySourceCode(String s){
        int[] nums = new int[26];
        //알파벳들 각각의 개수를 카운팅
        for(int i = 0; i < s.length(); i++){
            nums[s.charAt(i) - 'a']++;
        }
        //알파벳들 우선순위 큐에 삽입
        PriorityQueue<Alphabet> pq = new PriorityQueue<>();
        for(int i = 0; i < nums.length; i++){
            if(nums[i] > 0){
                pq.offer(new Alphabet((char)(i + 'a'), nums[i]));
            }
        }

        //재정렬하지 못한다면 빈 문자열 반환
        if(pq.peek().getCount() > (s.length() + 1) / 2) return "";

        char[] result = new char[s.length()];
        //가장 많이 나온 문자부터 재정렬
        int idx = 0;

        while(!pq.isEmpty()){
            Alphabet now = pq.poll();
            while(now.getCount() > 0){
                if(idx >= result.length) idx = 1;
                result[idx] = now.getValue();
                now.minusCount();
                idx += 2;
            }
        }

        return String.valueOf(result);
    }

    /**
     * 정답 코드
     */
    public static String solution(String s) {
        int[] nums = new int[26];
        //알파벳들 각각의 개수를 카운팅
        for(int i = 0; i < s.length(); i++){
            nums[s.charAt(i) - 'a']++;
        }
        //재정렬 할 수 있는지 아닌지 판별
        int maxCount = 0;
        int maxAlphabetIdx = 0;
        for(int i = 0; i < nums.length; i++){
            if(maxCount < nums[i]){
                maxCount = nums[i];
                maxAlphabetIdx = i;
            }
        }
        //재정렬하지 못할 경우 빈 문자열 반환
        if(maxCount > (s.length() + 1) / 2) return "";

        char[] result = new char[s.length()];
        //가장 많이 나온 문자 1씩 띄워서 넣기
        int idx = 0;
        while(nums[maxAlphabetIdx] > 0){
            result[idx] = (char)(maxAlphabetIdx + 'a');
            idx += 2;
            nums[maxAlphabetIdx]--;
        }
        //나머지 문자열 넣기
        for(int i = 0; i < nums.length; i++){
            //특정 문자를 다 소모할 때까지 반복
            while(nums[i] > 0){
                if(idx >= result.length) idx = 1;
                result[idx] = (char)(i + 'a');
                idx += 2;
                nums[i]--;
            }
        }

        return String.valueOf(result);
    }
}
