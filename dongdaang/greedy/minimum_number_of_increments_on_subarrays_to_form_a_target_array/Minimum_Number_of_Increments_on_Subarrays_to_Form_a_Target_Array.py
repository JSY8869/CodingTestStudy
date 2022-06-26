# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/


####################시간초과###################

class Solution:
    def minNumberOperations(self, target):
        N = len(target)
        now = [0] * N
        res = 0
        
        while now != target:
            indexes = []
            for i in range(N):
                if now[i] == target[i]:
                    indexes.append(i)
            if indexes:
                if len(indexes) > 1:
                    for i in range(len(indexes) - 1):
                        flag = False
                        for j in range(indexes[i] + 1, indexes[i + 1]):
                            now[j] += 1
                            flag = True
                        if flag:
                            res += 1
                flag = False
                for i in range(indexes[0]):
                    now[i] += 1
                    flag = True
                if flag:
                    res += 1
                flag = False
                for i in range(indexes[-1] + 1, N):
                    now[i] += 1
                    flag = True
                if flag:
                    res += 1
            else:
                for i in range(N):
                    now[i] += 1
                res += 1
        
        return res
                    
            
a = Solution()
print(a.minNumberOperations([1,2,3,2,1]))


###############솔루션##################

class Solution:
    def minNumberOperations(self, A):
        res = pre = 0
        for a in A:
            res += max(a - pre, 0)
            pre = a
        return res