# https://leetcode.com/problems/open-the-lock/


###########돌아가긴 하는데 애매함(5900ms)############

from collections import deque

class Solution:
    def openLock(self, deadends, target):    
        if '0000' in deadends:
            return -1
        def bfs():
            global cnt
            while queue:
                n = len(queue)      #현재 큐의 크기
                for _ in range(n):              #현재 큐의 크기만큼 시도한 후 cnt 1 증가
                    now = queue.popleft()       #now -> 현재 시도하는 번호
                    if now == target:
                        return cnt
                    for i in range(4):          #4자리 모두 시도
                        for j in range(2):      # +1, -1 모두 시도
                            next = now[:i] + str((int(now[i]) + dx[j]) % 10) + now[i+1:]    #next -> 변경된 번호
                            if next in deadends or visited[int(next)]:
                                continue
                            queue.append(next)
                            visited[int(next)] = True
                cnt += 1
            return -1
        
        dx = [-1, 1]    #숫자 한칸씩 변경해주기 위한 변수
        global cnt      #변경 횟수 기록해주는 변수
        cnt = 0
        queue = deque(['0000'])     #변경 가능한 번호 담아주는 큐
        visited = [False] * 10000   #이미 방문한 번호를 표시해주는 배열
        visited[0] = True
        
        return bfs()

a = Solution()
print(a.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], '8888'))




###################솔루션(600ms)###################

class Solution:
    def openLock(self, deadends, target):
        dead_set = set(deadends)
        queue = deque([('0000', 0)])    #변경된 횟수를 해당 번호와 튜플로 묶어서 큐에 저장
        visited = set('0000')           #이미 방문한 번호 세트로 저장

        while queue:
            (string, steps) = queue.popleft()
            if string == target:
                return steps
            elif string in dead_set:
                continue
            for i in range(4):
                digit = int(string[i])
                for move in [-1, 1]:        #move -> 번호 변경을 위한 변수
                    new_digit = (digit + move) % 10
                    new_string = string[:i]+str(new_digit)+string[i+1:]     #new_string -> 변경된 번호
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps+1))
        return -1