#https://leetcode.com/problems/find-all-people-with-secret/


#################솔루션 확인##################

from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson):
        
        class UnionFind:
            def __init__(self):         #parents와 ranks 생성
                self.parents = {}
                self.ranks = {}
                
            def insert(self, x):            #parents 딕셔너리에 현재 노드 추가, ranks 0으로 초기화
                if x not in self.parents:
                    self.parents[x] = x
                    self.ranks[x] = 0
                
            def find_parent(self, x):       #부모노드를 찾아주는 함수
                if self.parents[x] != x:
                    self.parents[x] = self.find_parent(self.parents[x])
                return self.parents[x]
            
            def union(self, x, y):          #부모노드를 바꿔주는 함수
                self.insert(x)
                self.insert(y)
                x, y = self.find_parent(x), self.find_parent(y)     #부모노드를 찾음
                if x == y:          #둘의 부모가 같으면 return
                    return 
                if self.ranks[x] > self.ranks[y]:       #rank가 높은 노드로 부모노드를 변경해줌
                    self.parents[y] = x
                else:
                    self.parents[x] = y
                    if self.ranks[x] == self.ranks[y]:      #rank가 같다면 둘중 하나 랭크 1 증가시켜줌
                        self.ranks[y] += 1
            
        time2meets = defaultdict(list)
        for x, y, t in meetings:
            time2meets[t].append((x, y))            #해당 시간에 있는 meeting을 딕셔너리에 추가
        time2meets = sorted(time2meets.items())     #시간 순으로 딕셔너리 값 정렬
 
        curr_know = set([0, firstPerson])           #현재 알고 있는 사람을 담아주는 set

        for time, meets in time2meets:
            uf = UnionFind()
            for x, y in meets:              #meeting 있는 사람끼리 union(부모노드를 확인 후 합쳐줌)
                uf.union(x, y)
            
            groups = defaultdict(set)       #같은 시간에 meeting을 가지는 모든 사람을 담아주는 groups 딕셔너리
            for idx in uf.parents:
                groups[uf.find_parent(idx)].add(idx)        #같은 부모노드를 가지는 값들끼리 set로 묶어줌
            
            for group in groups.values():       #각각의 그룹과 현재 알고 있는 사람을 세트 & 연산
                if group & curr_know:           #교집합이 존재하면 그룹 내 모든 사람을 curr_know에 넣어줌
                    curr_know.update(group)     #해당 시간에 그룹 내 한명이라도 비밀을 아는 사람이 있으면 그룹 내 모든 사람이 알 수 있으므로

        return list(curr_know)

a = Solution()
print(a.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))