package com.leetcode.string.wordbreak;

import java.util.*;

public class WordBreak {

    static class MySourceCode{

        public boolean wordBreak(String s, List<String> wordDict) {

            PriorityQueue<String> leftWord = new PriorityQueue<>();
            leftWord.offer(s);

            //처리해야 할 남은 문자열이 없을때까지 반복
            while(!leftWord.isEmpty()){
                String now = leftWord.poll();
                //원래 문자열 s를 사전에 있는 문자열들로 만들수 있다면
                if(now.isEmpty()) return true;

                for(int i = 0; i < now.length(); i++){
                    //현재까지 문자열이 사전에 존재하고, 처리할 문자열에 동일한 문자열이 없다면
                    if(wordDict.contains(now.substring(0, i+1)) && checkDuplicatedWord(leftWord, now, i)) {
                        leftWord.offer(now.substring(i+1));
                    }
                }
            }

            return false;
        }

        private boolean checkDuplicatedWord(PriorityQueue<String> leftWord, String now, int i) {
            return !leftWord.contains(now.substring(i +1));
        }
    }
}
