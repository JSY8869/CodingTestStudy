package com.leetcode.greedy;

import java.util.Arrays;
import java.util.Comparator;

/**
 * https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
 */
public class MinNumOfArrowsToBurstBalloons {

    public static class MySourceCode{

        public int findMinArrowShots(int[][] points) {
            //첫번째 x 좌표로 정렬
            Arrays.sort(points, Comparator.comparingInt(o -> o[0]));
            //화살의 개수, 최대출발 x좌표, 최소끝 x좌표 초기화
            int numsOfArrow = 1;
            int maxXStart = Integer.MIN_VALUE;
            int minXEnd = Integer.MAX_VALUE;

            for(int[] point : points){
                int xStart = point[0];
                int xEnd = point[1];

                maxXStart = Math.max(maxXStart, xStart);
                minXEnd = Math.min(minXEnd, xEnd);
                //교차점이 존재하지 않는다면 화살의 개수 하나 증가
                if(maxXStart > minXEnd){
                    numsOfArrow++;
                    maxXStart = xStart;
                    minXEnd = xEnd;
                }
            }

            return numsOfArrow;
        }
    }

    public static class Solution{

        public int findMinArrowShots(int[][] segments) {
            Arrays.sort(segments, Comparator.comparingInt(a -> a[1]));
            int ans = 0, arrow = 0;
            for (int i = 0; i < segments.length; i ++) {
                if (ans == 0 || segments[i][0] > arrow) {
                    ans ++;
                    arrow = segments[i][1];
                }
            }
            return ans;
        }
    }
}
