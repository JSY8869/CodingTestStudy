package com.leetcode.string.simplifypath;

import java.util.Stack;

public class SimplifyPath {

    static class MySourceCode {

        private static final char slash = '/';
        private static final String dot = ".";
        private static final String twoDot = "..";

        private Stack<String> stack = new Stack<>();

        public String simplifyPath(String path) {

            StringBuffer buffer = new StringBuffer();
            for(int i = 0; i < path.length(); i++){
                char now = path.charAt(i);
                if(now == slash || i == path.length()-1){
                    // TODO : 마지막 부분 처리
                    if(now != slash && i == path.length()-1) buffer.append(now);

                    String pathName = buffer.toString();
                    // TODO : 버퍼가 비었다면 무시
                    if(pathName.isEmpty()) continue;
                    // TODO : 한 개의 점이면 무시
                    if(pathName.equals(dot)) {
                        buffer = new StringBuffer();
                        continue;
                    }

                    // TODO : 두 개의 점이라면 스택에서 하나 제거
                    if(pathName.equals(twoDot)){
                        if(!stack.isEmpty()) stack.pop();
                    } else {
                        stack.push(pathName);
                    }

                    buffer = new StringBuffer();
                } else {
                    buffer.append(now);
                }
            }

            StringBuilder ans = new StringBuilder();
            for (String s : stack) {
                ans.append("/").append(s);
            }

            return ans.length() == 0 ? "/" : ans.toString();
        }
    }
}
