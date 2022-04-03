# 991. Broken Calculator
## 문제 설명
2는 곱하기 2, 1은 빼기 1이다.
최소로 사용해서 타겟을 만드는 방법을 구하라.

## 해결 방법
- startValue를 움직이는게 아니라 target을 움직이면 쉽다.
1. target을 2로 나눈 나머지가 1이면 +1 -> startValue를 -1 해준 것과 같은 의미
2. target을 2로 나눈 나머지가 0이면 나누기 2
3. target이 startValue와 같으면 끝
4. target이 startValue보다 작아지면 startValue를 -1 해주면서 count+1 해줘야 함
