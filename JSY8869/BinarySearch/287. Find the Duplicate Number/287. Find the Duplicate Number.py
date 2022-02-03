class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            print("fast", fast, "slow", slow)
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            print("fast2", fast, "slow2", slow)
            slow = nums[slow]
            fast = nums[fast]
        return slow

    
a = Solution()
print(a.findDuplicate([1,3,4,2,1]))