# Simulation - Car Pooling
## 문제풀이
* 문제풀이 전략
    * 우선순위 큐를 활용하여 목적지를 기준으로 처리

* 코드 설명
    1. trips 배열을 출발지를 기준으로 오름차순 정렬  

    2. 만약 처음 출발지에서 인원 수가 수용 능력 초과하면 False 리턴  

    3. heap에 (목적지, 인원 수)의 형태로 정보 저장  

    4. trips 배열을 순차적으로 돌면서 처리  

    5. 만약 다음 정류장 보다 목적지가 가까운 사람들 있으면 내려주기  
    ```
    while heap:
        if heap[0][0] <= start:
            tmp = heapq.heappop(heap)
            total -= tmp[1]
        else:
            break
    ```

    6. 현재 정류장에서 사람들 태울 수 있으면 태우기  
    ```
    if total + people <= capacity:
        total += people
        heapq.heappush(heap, (end, people))
    ```

    7.  trips 배열 끝까지 처리 했다면 True 리턴, 중간에 조건을 만족 못했으면 False 리턴