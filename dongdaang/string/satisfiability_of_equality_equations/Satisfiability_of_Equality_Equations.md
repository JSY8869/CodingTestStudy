# String - Satisfiability of Equality Equations
## 문제풀이
* 문제풀이 전략
    * 유니온 파인드를 활용해 문제 풀이
    * 변수를 숫자로 변환하여 활용

* 코드설명
    1. 변수들을 숫자로 변경(ex : a -> 0, b -> 1, c -> 2...)  
    ```
    var1 = ord(equation[0]) - 97
    var2 = ord(equation[3]) - 97
    ```

    2. 비교연산자가 '=='이라면 부모를 같게 만들어준다.  
    ```
    if equation[1] == '=':
        union(var1, var2)
    ```

    3. 비교연산자가 '!='인데 부모가 같다면 방정식을 만족하지 못하므로 False를 반환한다.  
    ```
    if equation[1] == '!':
        if find(var1) == find(var2):
            return False
    ```

    4. 모든 방정식을 만족한다면 True를 반환한다.