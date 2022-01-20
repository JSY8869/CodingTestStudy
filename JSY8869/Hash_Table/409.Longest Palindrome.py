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
        temp = False
        for i in range(len(value)):
            if value[i] % 2 == 0:
                result += value[i]
            else:
                result += value[i] - 1
                temp = True
        return result+temp



        

a = Solution()
print(a.longestPalindrome("abccccdd"))