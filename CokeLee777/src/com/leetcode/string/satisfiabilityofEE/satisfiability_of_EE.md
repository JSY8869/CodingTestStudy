## String - [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)

### 문제설명

- 두 개의 값을 비교하는 연산이 담겨있는 배열이 주어진다.
- 각 배열의 요소는 4자리의 문자열이다.
- 값은 모두 알파벳 소문자로 주어진다.

이 때, 모든 연산이 말이 되는 연산이고, 서로를 비교할 수 있다면 true, 아니면 false를 반환해라.

### 문제풀이

- 문제풀이 전략
  - 서로소 알고리즘
  - 그래프


- 문제풀이 설명
1. 부모 배열을 자신의 인덱스로 초기화한다.
2. '=='인 연산의 두 문자를 서로 연결한다.
3. '!='인 연산의 두 문자열이 이미 '=='이라면 false를 반환한다.
4. 3번이 부합하는 연산이 없다면 true를 반환한다.

