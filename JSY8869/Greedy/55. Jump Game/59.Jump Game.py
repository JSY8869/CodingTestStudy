class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = len(nums)-1
        for i in range(len(nums) - 1, -1, -1): # 탑다운 탐색
            if nums[i] + i >= temp:
                temp = i
        return temp == 0


a = Solution()
print(a.canJump([2,3,1,1,4]))