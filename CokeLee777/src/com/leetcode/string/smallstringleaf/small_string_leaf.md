## String - [Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/)

### 문제설명

- 이진트리의 root들이 주어진다. 각각의 node는 0부터 25까지의 숫자를 갖는데, 이는 알파벳 'a' 부터 'z'를 의미한다.
- 제일 밑의 노드부터 말단 노드까지의 최소 거리를 사전순으로 나열했을 때, 가장 사전순으로 빠른 경로를 구하여라.

### 문제풀이

- 문제풀이 전략
    - DFS
    - Reverse Sort

- 문제풀이 설명

먼저 최종값(ans)를 'z'의 8500번 반복한 문자열로 만든다. (사전순으로 가장 뒤에있음)

1. 현재 노드를 방문하여 알파벳을 뒤에 이어붙힌다.
   1. 자식 노드가 존재한다면 방문하고 1번으로 돌아가 반복한다.
   2. 자식노드가 존재하지 않는다면 현재 tmp값을 뒤집어서 최종값(ans)와 비교하고 사전순으로 앞서는 것으로 변경한다.

