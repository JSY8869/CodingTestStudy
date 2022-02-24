package com.leetcode.hashtable;

import java.util.*;

/**
 * https://leetcode.com/problems/sort-characters-by-frequency/
 */
public class SortCharactersByFrequency {

    public static class MySourceCode{

        class Alphabet implements Comparable<Alphabet>{
            private final char letter;
            private final int count;

            public Alphabet(char letter, int count) {
                this.letter = letter;
                this.count = count;
            }

            public char getLetter() {
                return letter;
            }

            public int getCount() {
                return count;
            }

            @Override
            public int compareTo(Alphabet o) {
                if(this.count > o.count) return -1;
                else return 1;
            }
        }

        public String frequencySort(String s) {
            //알파벳의 개수 세기
            Map<Character, Integer> charToCount = new HashMap<>();
            for(char x : s.toCharArray()){
                charToCount.put(x, charToCount.getOrDefault(x, 0) + 1);
            }
            //리스트에 삽입 후 나온 개수가 큰 순서대로 정렬
            List<Alphabet> alphabets = new ArrayList<>();
            for (Character x : charToCount.keySet()) {
                alphabets.add(new Alphabet(x, charToCount.get(x)));
            }

            Collections.sort(alphabets);

            //정렬된 문자들 개수만큼 반복해서 저장
            StringBuilder ans = new StringBuilder();
            for (Alphabet alphabet : alphabets) {
                char letter = alphabet.getLetter();
                int count = alphabet.getCount();
                //문자의 개수만큼 반복
                ans.append(String.valueOf(letter).repeat(count));
            }

            return ans.toString();
        }
    }

    public static class Solution{

        public String frequencySort(String s) {
            Map<Character, Integer> map = new HashMap<>();
            for (char c : s.toCharArray())
                map.put(c, map.getOrDefault(c, 0) + 1);

            List<Character> [] bucket = new List[s.length() + 1];
            for (char key : map.keySet()) {
                int frequency = map.get(key);
                if (bucket[frequency] == null) bucket[frequency] = new ArrayList<>();
                bucket[frequency].add(key);
            }

            StringBuilder sb = new StringBuilder();
            for (int pos = bucket.length - 1; pos >= 0; pos--)
                if (bucket[pos] != null)
                    for (char c : bucket[pos])
                        for (int i = 0; i < pos; i++)
                            sb.append(c);

            return sb.toString();
        }
    }
}
