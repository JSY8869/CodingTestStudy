package com.leetcode.hashtable;

import java.util.*;

/**
 * https://leetcode.com/problems/longest-palindrome/
 */
public class LongestPalindrome {

    public static int mySourceCode(String s) {
        HashMap<Character, Integer> map = new LinkedHashMap<>();
        boolean isOdd = false;
        //문자열의 길이가 1이라면
        if(s.length() == 1) return 1;

        for(int i = 0; i < s.length(); i++){
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }

        int result = 0;
        for (Integer value : map.values()) {
            //문자의 개수가 짝수라면 더한다
            if(value % 2 == 0){
                result += value;
                continue;
            }
            if(!isOdd) isOdd = true;
            //문자의 개수가 홀수라면 하나를 빼고 더한다
            result += (value-1);
        }

        return isOdd ? result + 1 : result;
    }

    /**
     * 정답 코드
     */
    public static int solution(String s){

        if(s == null || s.length() == 0) return 0;
        Set<Character> hashSet = new HashSet<>();
        int count = 0;

        for(int i = 0; i < s.length(); i++){
            if(hashSet.contains(s.charAt(i))){
                hashSet.remove(s.charAt(i));
                count++;
            } else {
                hashSet.add(s.charAt(i));
            }
        }

        return hashSet.isEmpty() ? count * 2 : count * 2 + 1;
    }
}
