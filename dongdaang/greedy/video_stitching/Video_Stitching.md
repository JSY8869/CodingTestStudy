# Greedy - Video Stitching
## 문제풀이
* 문제풀이 전략
    * 정렬

* 코드 설명
    1. clips를 start가 빠른 순, 간격이 작은 순으로 정렬  

    2. 만약 요구된 time을 초과하여 비디오가 커버 되었다면 break
    ```
    if covered[1] >= time:
        break
    ```

    3. 현재 클립이 아직 커버되지 않은 부분을 커버할 수 있다면 사용  
    ```
    if clips[i][1] > covered[1] and clips[i][0] <= covered[1]:
        covered = [0, clips[i][1]]
        used[i] = True
    ```

    4. 이전에 사용된 클립들 중, 현재 클립이 커버할 수 있는 범위 내에 있는 클립들을 미사용 상태로 변경  
    ```
    for j in range(i):
        if used[j]:
            if clips[j][0] == clips[i][0]:
                for k in range(j, i):
                    used[k] = False
            elif clips[j][0] < clips[i][0] <= clips[j][1]:
                for k in range(j + 1, i):
                    used[k] = False
    ```

    5. 만약 요구된 비디오량을 전부 커버하지 못했다면 -1 리턴  

    6. 만약 모두 커버했다면 사용된 클립 개수 리턴