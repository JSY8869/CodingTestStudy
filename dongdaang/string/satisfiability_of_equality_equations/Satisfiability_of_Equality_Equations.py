# https://leetcode.com/problems/satisfiability-of-equality-equations/


class Solution:
    def equationsPossible(self, equations):
        def find(x):
            if parent[x] == x:
                return x
            p = find(parent[x])
            parent[x] = p
            return parent[x]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return
            if x < y:
                parent[y] = x
            else:
                parent[x] = y
        
        parent = [i for i in range(26)]
        
        for equation in equations:
            var1 = ord(equation[0]) - 97
            var2 = ord(equation[3]) - 97
            if equation[1] == '=':
                union(var1, var2)
        
        for equation in equations:
            var1 = ord(equation[0]) - 97
            var2 = ord(equation[3]) - 97
            if equation[1] == '!':
                if find(var1) == find(var2):
                    return False
        
        return True

a = Solution()
print(a.equationsPossible(["a==b","b!=c","c==a"]))