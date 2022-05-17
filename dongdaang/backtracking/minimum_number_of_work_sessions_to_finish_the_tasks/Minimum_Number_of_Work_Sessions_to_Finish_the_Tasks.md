# Backtracking - Minimum Number of Work Sessions to Finish the Tasks
## 문제풀이
* 문제풀이 전략
    * 백트래킹 알고리즘을 활용하여 모든 경우 탐색

* 코드설명
    1. 재귀함수 진행 중 subsets의 개수가 현재 최소값보다 커진다면, 더 이상 진행 할 필요 없으므로 백트래킹  
    ```
    if len(subsets) >= res:
        return
    ```
    2. 모든 task를 수행한 경우, subsets의 개수 확인 후 최소값 갱신  
    ```
    if idx == N:
        res = min(res, len(subsets))
        return
    ```
    3. 현재 수행한 task와 합쳐질 수 있는 task라면 합친 후 재귀함수 진행  
    ```
    for i in range(len(subsets)):
        if subsets[i] + tasks[idx] <= sessionTime:
            subsets[i] += tasks[idx]
            backtracking(idx + 1)
            subsets[i] -= tasks[idx]
    ```
    4. 현재 수행한 task와 합쳐질 수 없는 task라면 새로운 task로 subsets에 추가해준 후 재귀함수 진행  
    ```
    subsets.append(tasks[idx])
    backtracking(idx + 1)
    subsets.pop()
    ```