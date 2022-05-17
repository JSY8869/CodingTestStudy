
class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        temp = []
        self.result = len(tasks)
        
        def func(index):
            if len(temp) >= self.result: # 중간 처리
                return
            
            if index == len(tasks): # 전체 탐색 완료
                self.result = min(self.result, len(temp))
                return
            
            for i in range(len(temp)): # 전체 탐색
                if temp[i] + tasks[index] <= sessionTime:
                    temp[i] += tasks[index]
                    func(index + 1)
                    temp[i] -= tasks[index]
            
            temp.append(tasks[index]) # 다음칸 추가
            func(index + 1)
            temp.pop()
        
        func(0)
        return self.result

a = Solution()
print(a.minSessions([3,1,3,1,1],8))