# Simulation - Find the Winner of an Array Game
## 문제풀이
* 문제풀이 전략
    * 구현

* 코드 설명
    1. 연승 해야하는 횟수가 배열 크기보다 크다면, 무조건 배열의 가장 큰 수가 우승  
    ```
    if k >= len(arr):
        return max(arr)
    ```

    2. p1(=arr[0])가 승리시, k번 승리했으면 winner, 아니라면 p2(=arr[1])을 뒤로 보내고 계속 실행  
    ```
    if p1 > p2:
        win_cnt[p1] += 1
        if win_cnt[p1] == k:
            winner = p1
            break
        else:
            arr.pop(1)
            arr.append(p2)
            continue
    ```

    3. p2가 승리시, k번 승리했으면 winner, 아니라면 p1을 뒤로 보내고 계속 실행
    ```
    else:
        win_cnt[p2] += 1
        if win_cnt[p2] == k:
            winner = p2
            break
        else:
            arr.pop(0)
            arr.append(p1)
    ```