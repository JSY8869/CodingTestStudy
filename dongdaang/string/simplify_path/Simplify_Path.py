# https://leetcode.com/problems/simplify-path/


class Solution:
    def simplifyPath(self, path):
        path_name = []
        path_exist = path.split('/')
        res = ''
        
        for p in path_exist:
            if p == '..':
                if path_name:
                    path_name.pop()
            elif p and p != '.':
                path_name.append(p)
                    
        for p in path_name:
            res += '/' + p

        if not res:
            return '/'
        
        return res

a = Solution()
print(a.simplifyPath("/home/"))