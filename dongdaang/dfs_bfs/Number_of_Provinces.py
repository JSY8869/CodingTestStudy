class Solution:
    def findCircleNum(self, isConnected):
        visited = [False] * len(isConnected)
        
        def dfs(pos):
            visited[pos] = True
            for i in range(len(isConnected[pos])):
                if isConnected[pos][i] == 1 and visited[i] == False:
                    dfs(i)
                    
        result = 0
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and visited[i] == False:
                    dfs(i)
                    result += 1
        return result
                    

a = Solution()
print(a.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))