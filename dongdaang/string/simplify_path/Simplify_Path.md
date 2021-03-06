# String - Simplify Path
## 문제풀이
* 문제풀이 전략
    * 모든 경로는 '/'로 나누어지므로 '/'로 경로를 나누어준다.
    * '.'은 현재 위치를 의미하므로 문제에서 의미 없는 문자열이다.
    * '..'은 이전 위치로 돌아가는 것을 의미하므로 가장 마지막 위치를 제거해준다.

* 코드설명
    1. 현재 주어진 경로를 '/'를 기준으로 나누어준다.  
    ```
    path_exist = path.split('/')
    ```

    2. 현재 가리키는 것이 '..'이라면 가장 마지막 위치를 제거해준다.  
    ```
    if p == '..':
        if path_name:
            path_name.pop()
    ```

    3. 현재 가리키는 것이 '.'이 아니라면 경로에 추가를 해준다.  
    ```
    elif p and p != '.':
        path_name.append(p)
    ```

    4. 문제에 주어진 조건대로 출력해준다.