package com.leetcode.dfsandbfs;

import java.util.LinkedList;
import java.util.Queue;

public class CourseSchedule {

    public boolean solution(int numCourses, int[][] prerequisites) {
        int[][] matrix = new int[numCourses][numCourses];
        int[] indegree = new int[numCourses];

        for (int i=0; i<prerequisites.length; i++) {
            int ready = prerequisites[i][0];
            int pre = prerequisites[i][1];      //선수과목
            //해당 선수과목이 처음이라면 선수과목 개수를 더한다
            if (matrix[pre][ready] == 0)
                indegree[ready]++; //duplicate case
            //선수과목 처리
            matrix[pre][ready] = 1;
        }

        int count = 0;
        Queue<Integer> queue = new LinkedList();
        //선수과목이 필요없는 과목을 큐에 삽입한다
        for (int i=0; i<indegree.length; i++) {
            if (indegree[i] == 0) queue.offer(i);
        }

        //큐가 빌때까지 반복
        while (!queue.isEmpty()) {
            int course = queue.poll();
            //수강한 과목의 개수를 더한다
            count++;
            for (int i=0; i<numCourses; i++) {
                //현재 과목이 선수과목인 과목이 있다면
                if (matrix[course][i] != 0) {
                    //현재 과목을 수강하고 선수과목이 없는 과목이 있다면 큐에 삽입한다
                    if (--indegree[i] == 0)
                        queue.offer(i);
                }
            }
        }
        //들은 과목과 전체과목을 비교
        return count == numCourses;
    }

}
