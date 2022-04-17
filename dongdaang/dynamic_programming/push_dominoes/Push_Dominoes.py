#https://leetcode.com/problems/push-dominoes/


class Solution:
    def pushDominoes(self, dominoes):
        n = len(dominoes)
        if n == 1:
            return dominoes

        force_point = []    #도미노를 넘어뜨린 지점만 담는 리스트
        res = []            #넘어뜨린 후 도미노 상태 담는 리스트
        ans = ''
        
        for i in range(n):
            res.append(dominoes[i])
            if dominoes[i] != '.':
                force_point.append(i)
        
        if not force_point:     #도미노를 넘어뜨린 지점이 없으면 도미노 그대로 반환
            return dominoes
        
        if dominoes[force_point[0]] == 'L':     #넘어뜨린 지점 중 가장 왼쪽에 있는 곳이 왼쪽으로 넘어진 경우
            for i in range(force_point[0]):
                res[i] = 'L'
        if dominoes[force_point[-1]] == 'R':        #넘어뜨린 지점 중 가장 오른쪽에 있는 곳이 오른쪽으로 넘어진 경우
            for i in range(n - 1, force_point[-1], -1):
                res[i] = 'R'
        
        for i in range(len(force_point) - 1):       #넘어뜨린 지점 사이의 경우의 수를 각각 처리
            if dominoes[force_point[i]] == 'L' and dominoes[force_point[i + 1]] == 'R':
                continue
            if dominoes[force_point[i]] == 'L' and dominoes[force_point[i + 1]] == 'L':
                for j in range(force_point[i] + 1, force_point[i + 1]):
                    res[j] = 'L'
            if dominoes[force_point[i]] == 'R' and dominoes[force_point[i + 1]] == 'R':
                for j in range(force_point[i] + 1, force_point[i + 1]):
                    res[j] = 'R'
            if dominoes[force_point[i]] == 'R' and dominoes[force_point[i + 1]] == 'L':
                tmp = force_point[i + 1] - force_point[i]
                m = tmp // 2
                if tmp % 2 == 0:
                    for j in range(force_point[i] + 1, force_point[i] + m):
                        res[j] = 'R'
                    for j in range(force_point[i + 1] - 1, force_point[i + 1] - m, -1):
                        res[j] = 'L'
                else:
                    for j in range(force_point[i] + 1, force_point[i] + m + 1):
                        res[j] = 'R'
                    for j in range(force_point[i + 1] - 1, force_point[i + 1] - m - 1, -1):
                        res[j] = 'L'
        
        for i in res:
            ans += i
            
        return ans
    
force_point = Solution()
print(force_point.pushDominoes('.L.R...LR..L..'))