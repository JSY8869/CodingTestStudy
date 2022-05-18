package com.leetcode.backtracking.minnumofworksessions;

import java.util.Arrays;

public class MinNumOfWorkSessions {

    static class Solution{

        private int res;
        private int maxSessionTime;
        private int[] tasks;
        private int[] sessions;

        public int minSessions(int[] tasks, int sessionTime) {
            Arrays.sort(tasks);
            this.res = tasks.length;
            this.maxSessionTime = sessionTime;
            this.tasks = tasks;
            this.sessions = new int[tasks.length];
            dfs(tasks.length - 1, 0);
            return res;
        }

        private void dfs(int taskID, int sessionCount) {
            if (sessionCount > res) return; //prune, if we didn't use prune, it will be 2200ms, if lucky you get ac
            if (taskID == tasks.length) {
                res = Math.min(res, sessionCount);
                return;
            }
            for (int i = 0; i < sessionCount; i++)
                if (sessions[i] + tasks[taskID] <= maxSessionTime) { //put task into old session bucket
                    sessions[i] += tasks[taskID];
                    dfs(taskID - 1, sessionCount);
                    sessions[i] -= tasks[taskID];
                }
            sessions[sessionCount] += tasks[taskID]; //put task into new empty session bucket
            dfs(taskID - 1, sessionCount + 1);
            sessions[sessionCount] -= tasks[taskID];
        }
    }
}
