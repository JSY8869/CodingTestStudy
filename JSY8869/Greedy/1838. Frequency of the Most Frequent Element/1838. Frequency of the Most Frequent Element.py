class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        max_freq = 1
        freq = 1
        left = 0
        
        for right in range(1, len(nums)):
            k -= (nums[right] - nums[right - 1]) * freq # freq만큼의 갯수를 증가시켜야 함
            freq += 1
            if k >= 0:
                max_freq = max(max_freq, freq)
            else:
                while k < 0:
                    k += nums[right] - nums[left]
                    left += 1
                    freq -= 1
        return max_freq


a = Solution()
print(a.maxFrequency([1,4,8,13],5))