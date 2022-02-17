class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        idx = 0
        while idx < len(s) and s.count(s[idx]) >= k : idx+=1
        if idx == len(s): return len(s)
        left, right = self.longestSubstring(s[:idx],k), self.longestSubstring(s[idx+1:],k)
        return max(left,right)