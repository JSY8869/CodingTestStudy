from collections import deque
class Solution:
    def getnextpasswords(self, password: str) -> list[str]:
        nextpassword = []
        
        for i, value in enumerate(password): # 한 자리씩
            for change in (-1, 1): # +1 -1 해줌
                rotatedValue = (int(value) + change) % 10
                
                nextpassword.append(password[:i] + str(rotatedValue) + password[i + 1:])
            
        return nextpassword
    
    def openLock(self, deadends, target):
        queue = deque([('0000', 0)]) # 현재 번호와 돌린 횟수
        seen = {'0000'} # 이미 들린 번호
        
        while queue:
            password, count = queue.popleft()
            
            if password == target: # 답을 찾은 경우
                return count
            
            if password in deadends: # deadends 예외
                continue
                
            for nextpassword in self.getnextpasswords(password):
                if nextpassword not in seen:
                    seen.add(nextpassword)
                    queue.append((nextpassword, count + 1))
                    
        return -1



a = Solution()
print(a.openLock(["0201","0101","0102","1212","2002"], "0202"))