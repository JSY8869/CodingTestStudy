class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]:
            return True
        elif nums[0] == 0:
            return False
        else:
            for i in range(1, len(nums)-1):
                if nums[i] == 0:
                    cnt = 0
                    for j in range(i):
                        if nums[j] > i - j:
                            break
                        else:
                            cnt += 1
                    if cnt == i:
                        return False
            return True
        
        
        #cnt 안쓰고 푸는 방법? -> 앞에서 하나만이라도 조건 만족하면 다음꺼 진행하는 코드 어떻게 짤까??