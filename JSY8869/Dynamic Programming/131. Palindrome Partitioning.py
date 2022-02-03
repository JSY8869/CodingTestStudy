class Solution:
    def partition(self, s):
        result = [] 
        partition = []

        def backTracking(i):
            if i >= len(s): # 종료
                result.append(partition.copy()) 
                return
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    partition.append(s[i:j+1])
                    backTracking(j + 1) # 재귀
                    partition.pop() # 재귀해서 결론이 나지 않은 경우 그냥 버림
        backTracking(0)
        return result
    
    def isPalindrome(self,s,left,right): # 왼쪽 오른쪽이 모두 같으면 palindrome
        while left < right:
            if s[left] != s[right]:
                return False
            left,right = left+1,right-1
        return True
        




a = Solution()
print(a.partition("aab"))