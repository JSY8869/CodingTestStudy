from collections import defaultdict
class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        N = len(favorite)
        people = 0
        index_to_like = defaultdict(list)
        like_to_index = defaultdict(list)
        bond = set() # 서로 좋아하는 경우 고정
        
        for a, b in enumerate(favorite):
            index_to_like[a].append(b)
            like_to_index[b].append(a)
            if favorite[b] == a:
                bond.add(tuple(sorted([a, b])))
        
        # 서로 좋아하는 경우와 서로 좋아하는 경우와 연결된 사람들을 연결
        def find(node, seen):
            total = 0
            for nei in like_to_index[node]:
                if nei not in seen:
                    seen.add(nei)
                    total = max(total, find(nei, seen) + 1)
            return total
        
        for a, b in bond:
            seen = {a, b}
            people += 2 + find(a, seen) + find(b, seen)
        
        
        # find max number of nodes in a Strongly Connected Component (SCC)
        def dfs(curr):
            nonlocal i, scc_max # 함수 밖에서 선언된 비전역변수를 전역변수 사용하듯 가져와서 사용
            stack.append(curr)
            on_stack[curr] = 1
            i += 1
            ids[curr] = low[curr] = i
            
            for nei in index_to_like[curr]:
                if ids[nei] == -1:
                    dfs(nei)
                if on_stack[nei]:
                    low[curr] = min(low[curr], low[nei])
            
            if ids[curr] == low[curr]:
                scc_length = 0
                while stack:
                    scc_length += 1
                    node = stack.pop()
                    on_stack[node] = 0
                    low[node] = ids[curr]
                    if node == curr:
                        break
                if scc_length > 2:
                    scc_max = max(scc_max, scc_length)
        scc_max = 0
        i = 0
        on_stack = [0] * N
        stack = []
        ids = [-1] * N
        low = [0] * N
        
        for i in range(N):
            if ids[i] == -1:
                dfs(i)
        
        return max(people, scc_max)




a = Solution()
a.maximumInvitations([3,0,1,4,1])