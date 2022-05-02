# Graph - Maximum Employees to Be Invited to a Meeting
## 문제풀이
* 문제풀이 전략
    * 그룹이 원형으로 이루어지는 경우, 상호 좋아하는 사람들이 있는 경우로 나눠서 처리
    * 각각의 경우에서의 최대값 두개를 비교하여 최종 최대값을 구함

* 코드 설명
    1. 그룹이 원형으로 이루어지는 경우 먼저 고려  

        1 - 1) dfs 방식으로 원형이 이루어지는 그룹 찾기  
        ```
        while seen[cur_people] == 0:
            seen[cur_people] = 1
            curset.add(cur_people)
            cur_people = A[cur_people]
        ```

        1 - 2) 탐색 이후 현 위치의 사람이 curset에 있으면 원형 그룹(즉, 원형 그룹의 시작점), 현재 탐색한 인원은 cursum  
                -> (cursum) - (start에서부터 원형 그룹 시작까지의 거리) = 원형 그룹 크기  
        ```
        if cur_people in curset:
            cursum = len(curset)
            
            while start != cur_people:
                cursum -= 1
                start = A[start]
            maxc = max(maxc, cursum)
        ```
    
    2. 그룹 내에 쌍방으로 좋아하는 사람들이 있는 경우  

        2 - 1) 쌍방으로 좋아하는 사람들의 쌍을 pair에 저장  
        ```
        pair = []
        visited = [0] * n
        for i in range(n):
            if A[A[i]] == i and visited[i] == 0:
                pair.append([i, A[i]])
                visited[i] = 1
                visited[A[i]] = 1
        ```

        2 - 2) 자신을 좋아하는 사람들을 딕셔너리 형태로 저장  
        ```
        child = defaultdict(list)
        for i in range(n):
            child[A[i]].append(i)
        ```

        2 - 3) 모든 쌍에 대하여 자신으로부터 이어진 사람들 수 조사  
                -> 한 쌍에 있는 두 사람 모두에 대해 조사해야 함  
        ```
        maxa = 0
        dq = deque()
        for cand in child[a]:
            if cand != b:
                dq.append([cand, 1])
        while dq:
            cur, n = dq.popleft()
            maxa = max(maxa, n)
            for nxt in child[cur]:
                dq.append([nxt, n + 1])
        ```
        
        2 - 4) 양 방향 모두 조사한 후 각각 더한 값에 쌍방으로 좋아하는 사람 더한 값이 결과값  
        ```
        res += 2 + maxa + maxb
        ```
    
    3. 두 경우의 값 중 최대값이 나올 수 있는 경우 중 최대값
        ```
        return max(maxc, res)
        ```