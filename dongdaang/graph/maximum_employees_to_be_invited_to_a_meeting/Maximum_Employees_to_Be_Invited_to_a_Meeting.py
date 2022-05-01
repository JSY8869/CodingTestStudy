#https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

from collections import defaultdict, deque


class Solution:
    def maximumInvitations(self, A):
        n, maxc = len(A), 0
        seen = [0] * n      #방문처리를 위한 배열
        for idx in range(n):
            if seen[idx] == 0:
                start = idx     #시작지점
                cur_people = idx    #현재위치
                curset = set()      #방문한 사람들
				
                while seen[cur_people] == 0:
                    seen[cur_people] = 1
                    curset.add(cur_people)
                    cur_people = A[cur_people]
                    
                if cur_people in curset:
                    cursum = len(curset)
					
                    while start != cur_people:
                        cursum -= 1
                        start = A[start]
                    maxc = max(maxc, cursum)
                                       
        pair = []       #쌍방으로 좋아하는 사람들 쌍
        visited = [0] * n
        for i in range(n):
            if A[A[i]] == i and visited[i] == 0:
                pair.append([i, A[i]])
                visited[i] = 1
                visited[A[i]] = 1

        res = 0
        child = defaultdict(list)       #자신을 좋아하는 사람을 value 리스트에 저장
        for i in range(n):
            child[A[i]].append(i)
        
        for a, b in pair:
            maxa = 0
            dq = deque()
            for cand in child[a]:
                if cand != b:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()       #cur : 현재위치, n : 조사한 인원 수
                maxa = max(maxa, n)
                for nxt in child[cur]:
                    dq.append([nxt, n + 1])

            maxb = 0
            dq = deque()
            for cand in child[b]:
                if cand != a:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxb = max(maxb, n)
                for nxt in child[cur]:
                    dq.append([nxt, n + 1])

            res += 2 + maxa + maxb

        return max(maxc, res)

a = Solution()
print(a.maximumInvitations([2,2,1,2]))