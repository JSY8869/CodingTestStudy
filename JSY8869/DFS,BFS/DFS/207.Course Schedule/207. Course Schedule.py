class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for x, y in prerequisites: # 각 인덱스에서 갈 수 있는 곳 저장
            graph[x].append(y)
        

        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        if visited[i] == -1: # 중복 방문
            return False
        if visited[i] == 1:
            return True
            
        visited[i] = -1

        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False

        visited[i] = 1
        return True

a = Solution()
print(a.canFinish(2, [[1,0]]))