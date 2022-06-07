## Simulation - [Find the Winner of an Array Game](https://leetcode.com/problems/find-the-winner-of-an-array-game/)

### 문제설명

- 모든 원소가 다 다른 정수형 배열과 정수 k가 주어진다.
- 인덱스 0, 1의 원소 두개가 게임을 시작하는데, 큰 원소가 이기게 되고, 작은 원소는 맨 뒤로 물러나게 된다.
- 게임은 하나의 원소가 k번 연속으로 이기면 종료된다.

이 때, 게임을 승리할 원소를 구하여라.

### 문제풀이

- 문제풀이 전략
    - 구현

- 문제풀이 설명

게임은 아주 간단하게 최근 승리자가 또 승리할 경우 winCount를 1증가시키고, 아니면 winCount를 1로 초기화하고 최근 승리자를
갱신한다. 이렇게 게임을 하다가 winCount가 k가 될 경우, 즉 k연승 할 경우 게임을 종료하고 승리자를 반환한다.
