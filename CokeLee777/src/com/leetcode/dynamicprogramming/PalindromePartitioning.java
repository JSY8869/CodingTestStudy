package com.leetcode.dynamicprogramming;

import java.util.ArrayList;
import java.util.List;

public class PalindromePartitioning {

    private static List<List<String>> results;
    private static ArrayList<String> temps;

    private static void backTrack(String s, int left){
        //완성되었다면 결과 리스트에 삽입
        if(temps.size() > 0 && left >= s.length()){
            ArrayList<String> copyTemps = (ArrayList<String>) temps.clone();
            results.add(copyTemps);
        }
        //조합 짜기
        for(int i = left; i < s.length(); i++){
            //앞뒤가 똑같은지 확인
            if(isPalindrome(s, left, i)){
                //한 문자라면
                if(left == i) temps.add(Character.toString(s.charAt(i)));
                //문자열이라면
                else temps.add(s.substring(left, i+1));
                //한 문자 뒤에서 다시 백트래킹
                backTrack(s, i+1);
                //백트래킹 후 마지막 문자 삭제
                temps.remove(temps.size() - 1);
            }
        }
    }

    private static boolean isPalindrome(String s, int left, int right){
        //한 문자라면
        if(left == right) return true;
        while(left < right){
            if(s.charAt(left) != s.charAt(right)) return false;
            left++; right--;
        }
        return true;
    }

    public static List<List<String>> partition(String s) {
        results = new ArrayList<>();
        temps = new ArrayList<>();
        backTrack(s, 0);
        return results;
    }
}
