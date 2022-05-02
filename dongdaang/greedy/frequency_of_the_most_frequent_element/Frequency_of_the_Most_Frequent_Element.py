#https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums, k):
        nums.sort(reverse=True)
        n = len(nums)
        l, r = 0, 0
        s = 0
        while r < n:
            s += nums[l] - nums[r]
            if s <= k:
                r += 1
            else:
                s -= (nums[l] - nums[l + 1]) * (r - l)
                l += 1
                r += 1
        
        return r - l

a = Solution()
print(a.maxFrequency([1,2,4], 5))