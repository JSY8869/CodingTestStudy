# ############시간초과 초드...#############

# class Solution:
#     def findMaxLength(self, nums):
#         s = sum(nums)
#         # if s == len(nums) // 2:
#         #     return len(nums)
#         i = 0
#         while True:
#             tmp = []
#             for j in range(i+1):
#                 tmp = nums[:j] + nums[len(nums)-i+j:]
#                 if s - sum(tmp) == (len(nums) - i) / 2:
#                     return len(nums) - i
#             i += 1
            
# a = Solution()
# print(a.findMaxLength([0,1,0,0,0,1,1,1,0,1,1]))

##############솔루션 확인###############

class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        max_length=0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index
        
        return max_length