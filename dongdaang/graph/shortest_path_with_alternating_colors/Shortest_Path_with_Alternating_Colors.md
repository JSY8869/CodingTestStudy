# Graph - Shortest Path with Alternating Colors
## 문제풀이
* 문제풀이 전략
    * bfs를 활용하여 연결된 노드끼리 거리 계산
    * 노드, 색깔, 거리를 튜플로 묶어서 저장
    * 빨간색, 파란색 경로로 모두 방문한 노드는 방문처리 해줌으로써 중복 제거
    * 연결된 노드는 거리 기록, 연결되지 않은 노드는 -1

* 코드 설명
    1. red = 0, blue = 1로 설정한 후, 연결 상태를 (다음 노드, 색깔, 거리)로 묶어서 graph에 저장  
        최초 거리는 모두 1이라고 초기화
    ```
    for edge in redEdges:
        graph[edge[0]].append((edge[1], 0, 1))
    for edge in blueEdges:
        graph[edge[0]].append((edge[1], 1, 1))
    ```
    2. 노드 0에서부터 시작
    3. 큐에서 하나씩 뽑아서 확인, 현재 노드 처음 방문하면 거리를 d로 바꿔줌  
        (해당 노드까지의 최단거리를 기록해주는 것이므로 최초에 방문할 때의 거리를 기록해주면 됨, 이후에는 기록할 필요 x)
    ```
    while queue:
        node, color, d = queue.popleft()
        if distance[node] == -1:
            distance[node] = d
    ```
    4. 현재 노드와 연결된 노드들 확인  
        -> 이전에 온 경로의 색깔과 다르면서, 해당 노드를 2번 이상 방문하지 않은 경우 이동할 수 있음  
        (색깔이 2가지이므로, 해당 노드에 방문할 수 있는 최대 횟수는 2번, 그 이상 방문은 최소값이 아니거나 무한루프를 생성하게 됨)
    ```
    for edge in graph[node]:
        if edge[1] != color and visited[node][edge[0]] < 2:
            visited[node][edge[0]] += 1
            queue.append((edge[0], edge[1], d + 1))
    ```
    5. bfs 수행 완료 후 distance 리스트를 반환