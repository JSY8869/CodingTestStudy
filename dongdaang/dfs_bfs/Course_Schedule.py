class Solution:
    def canFinish(self, numCourses, prerequisites):
        info = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            info[x].append(y)
        
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in info[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True