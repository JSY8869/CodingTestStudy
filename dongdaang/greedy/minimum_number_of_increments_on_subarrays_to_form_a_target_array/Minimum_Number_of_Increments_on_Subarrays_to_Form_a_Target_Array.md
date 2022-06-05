# Greedy - Minimum Number of Increments on Subarrays to Form a Target Array
## 문제풀이
* 문제풀이 전략
    * 탐색
    * 아이디어 추론

* 코드 설명  
    순차적으로 숫자 탐색  
    현재 숫자가 바로 앞에 있는 숫자보다 큰 경우 두 숫자의 차이 만큼 연산이 필요 -> 두 수의 차이만큼 res 증가  
    반대로 작다면 앞에 있는 숫자가 연산되는 동안 같이 연산 되었을 것이므로 res에 영향 X
    ```
    res = pre = 0
    for a in A:
        res += max(a - pre, 0)
        pre = a
    ```