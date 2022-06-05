
class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        result = target[0]
        for index, now in enumerate(target[1:]):
            if now > target[index]:
                result += (now - target[index])
        return result

        

a = Solution()
print(a.minNumberOperations([3,1,5,4,2]))