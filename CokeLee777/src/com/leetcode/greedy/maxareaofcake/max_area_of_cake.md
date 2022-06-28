## Greedy - [Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)

### 문제설명

- h x w 의 넓이를 가지고있는 사각형의 케잌이 주어진다.
- 두 개의 배열도 주어지는데 각각 케잌을 자를 좌표가 주어진다.

이 때, 자른 조각들중에 가장 큰 조각의 넓이를 구하시오.

### 문제풀이

- 문제풀이 전략
  - 정렬 
  - 최대값 갱신

- 문제풀이 설명

1. 케잌을 자르기 전에 좌표가 작은 순서대로 정렬한다.

```java
Arrays.sort(horizontalCuts);
Arrays.sort(verticalCuts);
```

2. 가로, 세로의 좌표대로 나누어 자른다음에 가장 크게 잘린 부분을 서로 곱한다. 단, 값이 너무 커질 수 있으므로 long
타입으로 곱하고 10^7 + 7 으로 나눈 나머지를 구한다음에 int 자료형으로 변환한다.

```java
return (int)(getMaxLength(horizontalCuts, h) * getMaxLength(verticalCuts, w) % (INF + 7)) ;
```

- 최대길이 구하는 코드

```java
private long getMaxLength(int[] cutArr, int len){

    long maxLen = cutArr[0];
    for(int i = 1; i < cutArr.length; i++){
        maxLen = Math.max(maxLen, cutArr[i] - cutArr[i-1]);
    }

    return Math.max(maxLen, len - cutArr[cutArr.length-1]);
}
```