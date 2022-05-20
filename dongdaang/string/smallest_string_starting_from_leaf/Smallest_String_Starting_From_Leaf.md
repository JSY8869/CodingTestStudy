# String - Smallest String Starting From Leaf
## 문제풀이
* 문제풀이 전략
    * dfs를 활용한 문제 풀이
    * leaf까지 탐색한 경우를 모두 찾은 후 비교

* 코드 설명
    1. 현재 노드의 left와 right가 모두 null이라면 현재 노드가 leaf 노드이므로, 현재까지 탐색한 문자열을 res에 저장  
    ```
    if not node.left and not node.right:
        res.append(chr(node.val + 97) + s)
        return
    ```
    2. 현재 노드에 left 또는 right가 존재하면, 해당 val을 기존 문자열 앞에 이어 붙이면서 dfs탐색 진행  
    ```
    if node.left:
        dfs(node.left, chr(node.val + 97) + s)
    if node.right:
        dfs(node.right, chr(node.val + 97) + s)
    ```
    3. leaf까지 탐색한 모든 경우가 담긴 res 리스트를 사전순으로 정렬 후 결과값 리턴