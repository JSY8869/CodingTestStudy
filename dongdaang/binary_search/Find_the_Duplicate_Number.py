class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1
        while low < high:
            cnt = 0
            mid = (high + low) // 2
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid
        return low