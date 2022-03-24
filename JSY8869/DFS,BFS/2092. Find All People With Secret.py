from collections import defaultdict, deque
class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        g = defaultdict(dict)
        for p1, p2, t in meetings: # 시간별 미팅 인원 정리
            g[t][p1] = g[t].get(p1, [])
            g[t][p1].append(p2)
            g[t][p2] = g[t].get(p2, [])
            g[t][p2].append(p1)

        known = {0, firstPerson} # 비밀을 아는 사람

        for t in sorted(g.keys()): # 시간순 정렬 후 for문
            seen = set() # 만난 사람
            for p in g[t]:
                if p in known and p not in seen: # 정보를 알고 있고 만난 사람에 없는 경우
                    q = deque([p])
                    seen.add(p) # 만난 사람에 추가
                    while q:
                        cur = q.popleft()
                        for nxt in g[t][cur]: # 해당 시간에 p랑 만난 사람
                            if nxt not in seen:
                                q.append(nxt) # 코로나 확진자처럼 역학조사
                                seen.add(nxt)
                                known.add(nxt)
        return known
a = Solution()
a.findAllPeople(6,[[1,2,5],[2,3,8],[1,5,10]],1)