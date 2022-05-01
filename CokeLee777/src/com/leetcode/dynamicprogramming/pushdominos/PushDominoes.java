package com.leetcode.dynamicprogramming.pushdominos;

public class PushDominoes {

    static class Solution{

        public String pushDominoes(String dominoes) {
            char[] a = dominoes.toCharArray();
            //투 포인터를 사용한 풀이
            for (int i = 0, L = -1, R = -1; i <= dominoes.length(); i++)
                //도미노의 끝점이거나 오른쪽으로 넘어지는 도미노라면
                if (i == a.length || a[i] == 'R') {
                    //마지막 끝 R이 L보다 인덱스가 크다면 모두 R로 치환
                    if (R > L)//R..R, turn all to R
                        while (R < i)
                            a[R++] = 'R';
                    R = i;
                    //도미노가 왼쪽으로 넘어지는 도미노라면
                } else if (a[i] == 'L')
                    //R이 아직 나오지 않았거나 마지막 L의 인덱스가 마지막 R보다 크다면
                    if (L > R || R == -1)//L..L, turn all to L
                        while (++L < i)
                            a[L] = 'L';
                    else { //R...L
                        L = i;
                        for (int lo = R + 1, hi = L - 1; lo < hi; ) {//one in the middle stays '.'
                            a[lo++] = 'R';
                            a[hi--] = 'L';
                        }
                    }
            return new String(a);
        }
    }

    static class Solution2{

        public String pushDominoes(String d) {
            d = 'L' + d + 'R';
            StringBuilder res = new StringBuilder();
            for (int i = 0, j = 1; j < d.length(); ++j) {
                if (d.charAt(j) == '.') continue;
                int middle = j - i - 1;
                if (i > 0)
                    res.append(d.charAt(i));
                if (d.charAt(i) == d.charAt(j))
                    for (int k = 0; k < middle; k++)
                        res.append(d.charAt(i));
                else if (d.charAt(i) == 'L' && d.charAt(j) == 'R')
                    for (int k = 0; k < middle; k++)
                        res.append('.');
                else {
                    for (int k = 0; k < middle / 2; k++)
                        res.append('R');
                    if (middle % 2 == 1)
                        res.append('.');
                    for (int k = 0; k < middle / 2; k++)
                        res.append('L');
                }
                i = j;
            }
            return res.toString();
        }
    }
}
