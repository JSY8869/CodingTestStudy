# Graph - Network Delay Time
## 문제풀이
* 문제풀이 전략
    * 네트워크는 방향그래프로 연결
    * 모든 노드에 신호가 전달 되는 시간은, 시작점으로부터 가장 먼 노드에 신호가 도착하는 시간
    * 최단경로 알고리즘을 활용하여 시작점으로부터 각 노드에 도착하는 최소 시간을 기록
    * 해당 값중 최대 값이 정답

* 코드 설명
    1. connections의 인덱스는 부모 노드, 해당 인덱스에 해당하는 리스트에 (자식 노드, 걸리는 시간) 삽입
    ```
    for info in times:
        connections[info[0]].append((info[1], info[2]))
    ```
    2. 힙 자료구조를 활용하여 현위치와 가장 가까운 순으로 탐색
        #### 시작점부터 현위치까지 걸린 시간이 이미 최소값이라면 continue
    ```
    while heap:
        distance, now = heapq.heappop(heap)
        if d[now] < distance:
            continue
    ```
    3. 현재 노드와 연결된 노드를 하나씩 탐색
        #### 시작점에서 현재 노드까지의 시간 + 다음 노드까지의 시간이 이전 값보다 더 작다면
        #### 최소 시간을 갱신해준 후, 힙에 해당 정보 삽입
    ```
    for next, weight in connections[now]:
        nextdistance = d[now] + weight
        if d[next] > nextdistance:
            d[next] = nextdistance
            heapq.heappush(heap, (nextdistance, next))
    ```