from pip import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        temp = {0:0}
        result = 0
        for index, value in enumerate(nums):
            if value == 0:
                count -= 1
            else:
                count += 1
            if count in temp:
                result = max(result, index-temp[count]) # index-temp[count] -> 현재 위치 - 전에 같은 count 값이었던 위치
            else:
                temp[count] = index
        return result



a = Solution()
print(a.findMaxLength([0,0,1,0,0,0,1,1]))
