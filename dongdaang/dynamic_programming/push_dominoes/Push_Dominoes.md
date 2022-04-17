# Dynamic Programming - Push Dominoes
## 문제풀이
* 문제풀이 전략
    * 도미노를 넘어뜨린 지점 사이만을 고려
    * 쓰러질 수 있는 경우의 수를 각각 처리

* 코드 설명
    1. 도미노의 길이가 1일 경우는 그대로 반환
    2. 도미노를 넘어뜨린 지점만 따로 뽑아서 저장
    3. 넘어뜨린 지점 중 가장 왼쪽에 있는 지점을 왼쪽으로 넘어뜨린 경우  
        -> 이 지점을 기준으로 왼쪽 끝까지 전부 왼쪽으로 쓰러뜨림  
    넘어뜨린 지점 중 가장 오른쪽에 있는 지점을 오른쪽으로 넘어뜨린 경우  
        -> 이 지점을 기준으로 오른쪽 끝까지 전부 오른쪽으로 쓰러뜨림
    ```
    if dominoes[force_point[0]] == 'L':
        for i in range(force_point[0]):
            res[i] = 'L'
    if dominoes[force_point[-1]] == 'R':
        for i in range(n - 1, force_point[-1], -1):
            res[i] = 'R'
    ```
    4. 넘어뜨릴 수 있는 경우의 수를 각각 처리  
        - L R -> 상관 없음
        - L L -> 모두 왼쪽으로 쓰러짐
        - R R -> 모두 오른쪽으로 쓰러짐
        - R L -> 사이에 있는 도미노 개수가 홀수개/짝수개인 경우에 따라 다름
        ```
        if dominoes[force_point[i]] == 'R' and dominoes[force_point[i + 1]] == 'L':
            tmp = force_point[i + 1] - force_point[i]
            m = tmp // 2
            if tmp % 2 == 0:
                for j in range(force_point[i] + 1, force_point[i] + m):
                    res[j] = 'R'
                for j in range(force_point[i + 1] - 1, force_point[i + 1] - m, -1):
                    res[j] = 'L'
            else:
                for j in range(force_point[i] + 1, force_point[i] + m + 1):
                    res[j] = 'R'
                for j in range(force_point[i + 1] - 1, force_point[i + 1] - m - 1, -1):
                    res[j] = 'L'
        ```
    5. 모두 쓰러뜨린 후 결과 출력