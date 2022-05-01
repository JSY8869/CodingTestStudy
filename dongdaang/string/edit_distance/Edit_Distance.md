# String - Edit Distance
## 문제풀이
* 문제풀이 전략
    * dynamic programming 활용
    * insert, delete, replace 세가지 경우를 비교하여 최소인 경우 선택
    * 각 단어의 각 문자끼리 서로 비교
    * 모두 비교 후 최소 값 출력

* 코드 설명
    1. 최소 값을 기록해줄 table 생성
    2. 각 자리 문자 모두 비교  
        - 같은 문자일 경우 -> 각 단어의 이전 문자들까지 비교한 값 그대로 가져옴
        - 다른 문자일 경우 -> 이전 문자 비교에서 insert, delete, replace한 세가지 경우 중 최소값에 +1한 값을 저장  
        (가로 줄이 insert, 세로 줄이 delete, 대각선이 replace)
    ```
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
    ```
    3. 모든 문자 비교 후 비교 횟수 반환