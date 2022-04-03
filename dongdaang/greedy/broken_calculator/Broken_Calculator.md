# Greedy - Broken Calculator
## 문제풀이
* 문제풀이 전략
    * x2를 최대한 많이 해야함
    * target을 감소시켜가며 startValue와 비교


* 코드 설명
    1. startValue와 target이 같으면 0 리턴
    ```
    if startValue == target:
        return 0
    ```
    2. startValue가 target보다 크면 1씩 빼기만 할 수 있으므로,  결론적으로 startValue - target와 같음
    ```
    elif startValue > target:
        return startValue - target
    ```

    3. startValue에서 x2를 해 나아갔을 때 가능한 모든 수를 array에 담아줌
    ```
    while startValue < target:
        array.append(startValue)
        startValue *= 2
    ```

    4. target이 2의 배수이면 나누기 2, 아니면 1을 더해줌
        #### (startValue 기준으로는 1씩 뺄 수 있기 때문)
    ```
    while True:
        if target % 2 == 0:
            target //= 2
        else:
            target += 1
        cnt += 1
    ```

    5. 만약 array에 현재 target값이 있는 경우, 현재까지 cnt에 array에서 현재 target의 인덱스를 더해서 반환해줌
        #### (startValue에서 현재 target값까지 오직 x2만 해서 도달할 수 있기 때문)
        #### 만약 array에 가능한 target값 없으면, startValue에서 현재 target값까지 뺀 후 cnt를 더한 값이 정답
    ```
    if target in array:
        return cnt + array.index(target)
    if target < array[0]:
        return cnt + array[0] - target
    ```