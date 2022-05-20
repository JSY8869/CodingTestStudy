# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/


class Solution:
    def minSessions(self, tasks, sessionTime):
        subsets = []
        N = len(tasks)
        global res
        res = N
        
        def backtracking(idx):
            global res
            
            if len(subsets) >= res:
                return
            
            if idx == N:
                res = min(res, len(subsets))
                return
            
            for i in range(len(subsets)):
                if subsets[i] + tasks[idx] <= sessionTime:
                    subsets[i] += tasks[idx]
                    backtracking(idx + 1)
                    subsets[i] -= tasks[idx]
            
            subsets.append(tasks[idx])
            backtracking(idx + 1)
            subsets.pop()
        
        backtracking(0)
        
        return res


################시간초과 코드###############
class Solution:
    def minSessions(self, tasks, sessionTime):
        def backtracking(time, cnt):
            global res
            if cnt > res:
                return
            
            if all(checked):
                if cnt < res:
                    res = cnt
                return
            
            for i in range(N):
                if checked[i]:
                    continue
                if time + tasks[i] > sessionTime:
                    backtracking(0, cnt + 1)
                else:
                    checked[i] = True
                    backtracking(time + tasks[i], cnt)
                    checked[i] = False
        
        N = len(tasks)
        checked = [False] * N
        global res
        res = 15
        
        backtracking(0, 1)
        
        return res
            

a = Solution()
print(a.minSessions([1,2,3,4,5], 15))