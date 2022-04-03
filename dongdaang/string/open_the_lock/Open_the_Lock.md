# String - Open the Lock
## 문제풀이
* 문제풀이 전략
    * 0000부터 target값까지 탐색
    * deadends 또는 이미 확인한 숫자 제외 후 bfs 방식으로 탐색
    * 탐색하는 동안 변경 횟수 기록

* 코드 설명
    1. 현재 큐에는 이전 번호에서 변경 가능한 번호들이 들어있음
        #### 현재 큐의 크기만큼 탐색 수행한 후 cnt 1 증가
        #### 현재 값이 target이라면 cnt 리턴
    ```
    while queue:
        n = len(queue)
        for _ in range(n):
            now = queue.popleft()
            if now == target:
                return cnt
    ```
    2. 4자리 번호의 각 자리를 +1, -1 한 번호 중, 가능한 번호만 queue에 삽입
        #### 해당 번호 방문 기록 표시
    ```
    for i in range(4):
        for j in range(2):
            next = now[:i] + str((int(now[i]) + dx[j]) % 10) + now[i+1:]
            if next in deadends or visited[int(next)]:
                continue
            queue.append(next)
            visited[int(next)] = True
    ```
    3. target에 도달하지 못했는데 queue가 비었다면, 도달 가능하지 못한 target이므로 -1 리턴