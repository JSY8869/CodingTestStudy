# Greedy - Maximum Number of Events That Can Be Attended
## 문제풀이
* 문제풀이 전략
    * 우선순위 큐를 활용한 문제풀이
    * 이벤트의 endDay가 빠른 이벤트부터 참여
    * 이벤트가 시작하는 날짜만을 따로 저장하여 실행시간 단축
    
* 코드설명
    1. 이벤트가 시작하는 날짜를 key, 해당 날짜에 시작되는 모든 이벤트를 value로 하는 dates 딕셔너리 생성  
        이벤트가 진행되는 마지막 날짜를 last_date로 설정  
    ```
    for event in events:
        dates[event[0]] += 1
        if event[1] > last_date:
            last_date = event[1]
    ```
    2. 만약 이벤트가 시작될 수 있는 날짜면, 조건에 해당되는 이벤트를 (endDay, 이벤트) 형식으로 heap에 저장  
    다음 탐색시에 더 빠른 동작을 위해, 탐색을 마친 지점의 index를 갱신해줌  
    ```
    for date in range(1, last_date + 1):
        if date in dates.keys():
            for i in range(index, index + dates[date]):
                    heapq.heappush(heap, (events[i][1], events[i]))
            index += dates[date]
    ```
    3. heap에서 꺼낸 이벤트에 참여할 수 있다면 참여, 참여할 수 없다면 제거하고 heap에서 다시 뽑기  
    ```
    while heap:
        current_meeting = heapq.heappop(heap)
        if current_meeting[1][0] <= date <= current_meeting[1][1]:
            res += 1
            break
    ```
    4. 참여한 총 이벤트 수인 res를 리턴