# String - Word Break
## 문제풀이
* 문제풀이 전략
    * dynamic programming 활용
    * 단어의 처음부터 진행하며, 현재까지의 문자열이 조합 가능한지 확인

* 코드 설명
    1. 문자열과 같은 길이의 배열 dp 생성  

    2. 만약 i번째 문자까지의 문자열이 wordDict에 존재한다면, 해당 위치까지의 문자는 조합 가능하므로 dp[i] = 1로 표시  

    3. dp[0] ~ dp[i] 중에서 값이 1인 경우 중, 그 위치에서 s[i]까지의 문자로 이루어진 문자열이 wordDict에 존재한다면,  
    단어가 조합 가능하다는 뜻이므로 dp[i] = 1로 표시  
    ```
    for j in range(i):
        if dp[j] == 1:
            if s[j + 1:i + 1] in wordDict:
                dp[i] = 1
    ```

    4. dp[-1]이 1이라면, 전체 문자열이 wordDict에 존재하는 단어들로 조합 가능하다는 뜻이므로 True 리턴  
    그렇지 않으면 False 리턴