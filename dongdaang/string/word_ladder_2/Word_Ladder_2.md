# String - Word Ladder 2
## 문제풀이
* 문제풀이 전략
    * dfs, bfs를 활용하여 문제 풀이
    * bfs 방식으로 인접한 단어 탐색
    * dfs 방식으로 부모를 찾아가며 path 탐색
    * 가능한 모든 path가 정답

* 코드 설명
    1. 탐색을 진행한 노드들을 wordList에서 제외  
    ```
    while curr_level:
            wordList -= curr_level
            next_level = set()
    ```

    2. 현재 탐색하는 단어와 인접한 단어(new_word)가 wordList에 있는지 검사  
        만약 존재한다면, next_level 집합에 해당 단어 추가, parents 딕셔너리에 new_word의 부모 단어 추가  
    ```
     for word in curr_level:
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in wordList:
                    next_level.add(new_word)
                    parents[new_word].append(word)
    ```

    3. 만약 next_level 집합에 endWord가 있다면, 최소 경로의 답을 찾았다는 뜻이므로 break  
        아니라면 같은 방식으로 계속 진행  
    ```
    if endWord in next_level:
        break
    curr_level = next_level
    ```

    4. parents 딕셔너리에 저장된 부모 단어들을 endWord부터 찾아 가며 path 저장  
        가능한 모든 path가 정답  
    ```
    def dfs(word, path):
        if word == beginWord:
            path.append(word)
            res.append(path[::-1])
        else:
            for p_word in parents[word]:
                dfs(p_word, path + [word])
    dfs(endWord, [])
    ```