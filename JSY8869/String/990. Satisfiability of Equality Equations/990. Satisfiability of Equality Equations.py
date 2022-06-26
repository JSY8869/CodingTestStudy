
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        
        def findParent(now): # 부모 찾기
            if now != parent[now]: 
                parent[now] = findParent(parent[now])
            return parent[now]
        
        parent = {}
        for i in range(97,123):
            parent[chr(i)] = chr(i) # chr -> 아스키코드를 문자열로
            
        for eq in equations: # 부모노드를 연결
            if eq[1] == "=":
                parent[findParent(eq[0])] = findParent(eq[3])

        for eq in equations:
            if eq[1] == '!' and findParent(eq[0]) == findParent(eq[3]):
                return False
        return True
    
    
a = Solution()
print(a.equationsPossible(["a==b","b!=a"]))