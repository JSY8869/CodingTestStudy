## Greedy - [Minimum Number of Increments on Subarrays to Form a Target Array](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/)

### 문제설명

- 정수형 배열 target이 주어진다.
- 처음 시작할 때, 0으로 채워져있고, target 배열과 크기가 동일한 정수형 배열로 시작한다.
- 연속된 인덱스의 배열을 동시에 1씩 증가시킬 수 있다.

이 때, 초기의 배열을 target 배열과 동일하게 만들 수 있는 연산 횟수의 최소값을 구하여라.

### 문제풀이

- 문제풀이 전략
  - Dynamic Programming

- 문제풀이 설명
  - 직전의 원소가 0인지 아닌지로 판단한다.

**초기 설정**

초기에 0번째 DP 원소를 target[0]으로 초기화한다.

```java
int[] dp = new int[target.length];
dp[0] = target[0];
```

**Dynamic Programming 수행**

반복문을 돌면서 직전의 원소가 0이 아닐경우와 0일경우로 나누어 생각한다.

1. 0일 아닐경우
   1. 숫자가 증가하는 원소라면 직전의 원소의 차이 만큼 더한다.
   2. 숫자가 감소하는 원소라면 직전의 DP값과 동일하다.
2. 0일 경우
   1. 해당 원소의 값 만큼 더한다.

```java
    for(int i=1;i<target.length;i++){
        // 직전의 원소가 0이 아닐경우
        if(target[i-1]!=0){
            if(target[i]>target[i-1])dp[i]+=dp[i-1]+(target[i]-target[i-1]);
            else dp[i]=dp[i-1];
        }else{
        dp[i]+=dp[i-1]+target[i];
        }
    }
```