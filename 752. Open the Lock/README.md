# 752. Open the Lock
## 문제 설명
번호 자물쇠에서 주어진 번호(deadends)를 거치지 않고 답을 찾는데 걸리는 시간을 구하는 문제

단, 시간은 한 번 움직일 때 1씩 흐름
## 풀이
- BFS사용
- 이미 탐색한 번호는 `seen`에 저장
- 다음으로 탐색할 번호는 `getnextpasswords` 함수를 통해 구함
- `getnextpasswords` 함수에서는 각 자리 번호를 +1, -1 이동시켜 list로 반환함
- 반환받은 번호에서 이미 탐색한 번호가 아닌 경우만 `queue`, `seen`에 저장하고 다시 탐색, `count + 1`
- 답을 찾은 경우 `count` 반환