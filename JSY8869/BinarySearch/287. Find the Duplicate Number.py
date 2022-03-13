class Solution(object):
    def findDuplicate(self, nums): # linked list cycle detection algorithm
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    
a = Solution()
print(a.findDuplicate([1,3,4,2,1]))