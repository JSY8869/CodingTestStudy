# 1526. Minimum Number of Increments on Subarrays to Form a Target Array
## 문제 설명
- target 배열과 initial 배열이 주어짐
- initial 배열은 모든 값이 0
- 한번에 하나의 subarray를 initial에서 선택해서 1씩 증가시킬 수 있음
- target array와 같아지기 위해 몇 번 증가시켜야 하는가를 반환
## 풀이 방법
- result를 1번째 숫자부터 시작
- 오른쪽으로 1칸씩 이동하면서 전 값보다 큰 경우 커진 만큼 result에 더함
- 올라갈때는 더하고 내려갈때는 넘어간다.
- 올라간 계단 갯수를 더하는 문제랄까?