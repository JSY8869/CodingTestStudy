# Greedy - Maximum Number of Eaten Apples
## 문제풀이
* 문제풀이 전략
    * 힙 구조를 활용해 날짜가 가장 적게 남은 사과부터 먹을 수 있게 처리
    * 하루가 지날 때 마다 날짜 수 카운트
    * 사과를 수확할 수 있는 상황에서는 사과 수확, 그 후 사과 하나씩 먹기
    * 모든 사과 수확한 후에는 힙에 있는 사과 계속 꺼내서 먹기
    * 힙이 빌 때 까지 수행

* 코드 설명
    1. 사과 수확 후 힙에 저장  
        -> 수확 당시 남은 일수에 수확한 날을 더한 것과 사과 개수를 튜플로 묶어서 저장
    ```
    for i in range(n):
        heapq.heappush(heap, (days[i] + i, apples[i]))
    ```
    2. 남은 일수 가장 작은 사과 선택, 사과가 1개 이상이고 안 상했으면 먹음, 조건에 해당 안되면 다시 뽑음  
        먹은 후 사과가 1개 이상이면 다시 힙에 저장
    ```
    while heap:
        now = heapq.heappop(heap)
        if now[0] - day_cnt > 0 and now[1] > 0:
            next = (now[0], now[1] - 1)
            if next[1] > 0:
                heapq.heappush(heap, next)
            apple_cnt += 1
            break
    ```
    3. 먹은 사과 개수 +1, 지난 날짜 수 +1
    4. 수확할 사과가 없으면 힙에 남아있는 사과 먹기
    5. 먹을 수 있는 모든 사과를 먹었으면(힙이 비었으면) 종료, 먹은 사과 개수 반환