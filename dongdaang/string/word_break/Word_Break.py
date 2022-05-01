# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict):
        n = len(s)
        dp = [0] * n
        for i in range(n):
            if s[:i + 1] in wordDict:
                dp[i] = 1
            for j in range(i):
                if dp[j] == 1:
                    if s[j + 1:i + 1] in wordDict:
                        dp[i] = 1
        if dp[-1]:
            return True
        else:
            return False
                    
a = Solution()
print(a.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))