# Greedy - Frequency of the Most Frequent Element
## 문제풀이
* 문제풀이 전략
    * 누적합(prefix sum), 투포인터 활용

* 코드 설명
    1. 주어진 배열을 reverse  
    
    2. 투포인터로 현재 두개의 포인터둘의 차이를 누적해서 더함  

    3. 만약 누적합(s)이 k보다 작다면, 아직 가능한 연산 횟수가 남아 있다는 의미  
    -> 오른쪽 포인터를 1 증가  

    4. 만약 누걱합이 k보다 크다면, 연산 가능 횟수를 초과했다는 의미  
    -> 누적합을 현재 투포인터의 값에 해당하도록 조정, 두 포인터 모두 증가  

    5. r이 배열의 끝에 도달했을 때 r - l 값을 리턴
