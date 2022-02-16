##################솔루션 확인####################

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:              #문자열에서 조건 해당 안되는 문자 기준으로 나눠서 각각 다시 조사
                return max(self.longestSubstring(t, k) for t in s.split(c))     #그 중 최대 값 반환
        return len(s)