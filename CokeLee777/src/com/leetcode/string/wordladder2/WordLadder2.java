package com.leetcode.string.wordladder2;

import java.util.*;
import java.util.stream.Collectors;

public class WordLadder2 {

    static class Solution {

        public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
            List<List<String>> res = new ArrayList<>();
            Set<String> set = new HashSet<>(wordList);
            Deque<List<String>> q = new ArrayDeque<>();
            q.addLast(Arrays.asList(beginWord));
            set.remove(beginWord);
            while (!q.isEmpty()) {
                int size = q.size();
                Set<String> toDelete = new HashSet<>();
                while (size-- > 0) {
                    List<String> path = new ArrayList<>(q.removeFirst());
                    String curWord = path.get(path.size()-1);
                    // TODO : 현재 단어에서 한 자리씩 바꿔가면서 존재하는 단어라면 삽입
                    for (int i = 0; i < curWord.length(); ++i) {
                        for (char c = 'a'; c <= 'z'; ++c) {
                            StringBuilder newWordSb = new StringBuilder(curWord);
                            newWordSb.setCharAt(i, c);
                            String newWord = newWordSb.toString();
                            if(set.contains(newWord)) {
                                path.add(newWord);
                                // TODO : 최종 목적지에 도달했다면 결과리스트에 저장
                                if (newWord.equals(endWord)) {
                                    res.add(new ArrayList<>(path));
                                }
                                q.addLast(new ArrayList<>(path));
                                path.remove(path.size()-1);
                                toDelete.add(newWord);
                            }
                        }
                    }
                }
                for (String word : toDelete) {
                    if (set.contains(word)) {
                        set.remove(word);
                    }
                }
            }
            return res;
        }
    }

    //시간초과..
    static class MySourceCode {

        private List<List<String>> ans = new ArrayList<>();
        private List<String> tmp = new ArrayList<>();
        private int minLength = Integer.MAX_VALUE;

        public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
            // TODO : 리스트에 endWord가 존재하지 않는다면 빈 리스트 반환
            if(!wordList.contains(endWord)) return new ArrayList<>();

            tmp.add(beginWord);
            dfs(beginWord, endWord, wordList);

            return ans;
        }

        public void dfs(String word, String endWord, List<String> wordList){
            // TODO : 경로가 원래 존재하는 경로보다 긴 경로라면 무시
            if(tmp.size() > minLength) return;

            // TODO : 문자열이 최종 문자열에 도착하면 리스트에 삽입
            if(word.equals(endWord)){
                if(tmp.size() < minLength) ans.clear();
                minLength = tmp.size();
                ans.add(new ArrayList<>(tmp));
                return;
            }

            // TODO : 백트래킹 수행
            for(int i = 0; i < word.length(); i++){
                String prefix = word.substring(0, i);
                String suffix = word.substring(i + 1);

                List<String> filteredWord = wordList.stream()
                        .filter(w -> w.startsWith(prefix) && w.endsWith(suffix))
                        .filter(w -> !tmp.contains(w))
                        .collect(Collectors.toList());

                for (String fw : filteredWord) {
                    tmp.add(fw);
                    dfs(fw, endWord, wordList);
                    tmp.remove(tmp.size() - 1);
                }
            }
        }
    }
}
