package com.leetcode.greedy.videostitching;

import java.util.Arrays;
import java.util.Comparator;

public class VideoStitching {

    static class MySourceCode{

        public int videoStitching(int[][] clips, int time) {
            // TODO : 시작시간을 기준으로 오름차순 정렬, 같으면 끝나는 시간이 큰 순서대로 정렬
            Arrays.sort(clips, (o1, o2) -> {
                if(o1[0] < o2[0]) return -1;
                else if(o1[0] == o2[0]) return o2[1] - o1[1];
                else return 1;
            });

            //시작부분이 존재하지 않는다면 -1반환
            if(clips[0][0] != 0) return -1;

            int segment = 1;
            int[][] editedVideo = new int[clips.length+1][2];
            for (int[] clip : clips) {
                // TODO : 다음 편집점이 필요하다면 -> 현재 클립이 전 클립과 이어지지 않고 끝나는 시간이 더 뒤에 끝난다면
                if(editedVideo[segment-1][1] < clip[0] && editedVideo[segment][1] < clip[1]) segment++;
                // TODO : 전의 편집점과 이어지고, 더 늦게 끝나는 편집점이라면 -> 세그먼트 업데이트
                if(clip[1] > editedVideo[segment][1]){
                    editedVideo[segment][0] = clip[0];
                    editedVideo[segment][1] = clip[1];
                }

                // TODO : 런타임 시간이 이어지지 않는다면 종료
                if(editedVideo[segment-1][1] < editedVideo[segment][0]) return -1;

                // TODO : 편집 중간에 이미 원하는 시간만큼의 비디오 클립을 완성했다면 종료
                if(editedVideo[segment][1] >= time) return segment;
            }

            // TODO : 비디오 클립을 완성할 수 없다면 -1반환
            return editedVideo[segment][1] >= time ? segment : -1;
        }
    }
}
