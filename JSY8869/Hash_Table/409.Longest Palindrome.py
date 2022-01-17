class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        count = Counter(s)
        value = list(count.values())
        result = 0
        temp = 0
        for i in range(len(value)):
            if value[i] % 2 == 0:
                result += value[i]
                value[i] = 0
            if value[i] % 2 != 0:
                result += value[i]-1
                temp = 1
        return result+temp



        

a = Solution()
print(a.longestPalindrome("abccccdd"))