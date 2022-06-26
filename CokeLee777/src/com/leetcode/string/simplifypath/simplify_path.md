## String - [Simplify Path](https://leetcode.com/problems/simplify-path/)

### 문제설명

- '/'로 시작하는 URL의 절대 경로가 주어진다.
- '.'의 의미는 현재 디렉토리를 의미한다.
- '..'의 의미는 현재 디렉토리의 한 단계 상위 디렉토리를 의미한다.
- '//'의 의미는 '/'와 동일하다.

이 때, 다음 조건을 만족하도록 경로를 간단하게 만들어라.
- 경로는 '/'로 시작한다.
- 두 개의 디렉토리는 '/'으로 구분되어있다.
- 경로는 '/'로 끝나지 않는다.
- 경로는 디렉토리나 파일명으로 구성된다. '.'이나 '..'이 없어야 한다.
- '...'도 디렉토리, 파일명으로 취급한다.

### 문제풀이

- 문제풀이 전략
    - Stack
    - 문자열
    
- 문제풀이 설명
1. 문자열을 하나씩 확인하면서 슬래쉬('/')가 나올때까지 버퍼에 넣는다.
2. 슬래쉬('/')가 나오면 비교
   1. 버퍼가 비었다면 무시한다.
   2. 버퍼에 '.'이 들어있다면 버퍼를 비우고 무시한다.
   3. 버퍼에 '..'이 들어있고, 스택이 비어있지 않다면 스택에서 하나를 꺼낸다.
   4. 이외의 경우에는 스택에 버퍼에 있는 문자열을 삽입한다.

### 이외의 전략

**마지막 부분이 슬래쉬('/')로 끝나지 않는것을 고려하여 마지막 부분을 처리한다.**

```java
if(now != slash && i == path.length()-1) buffer.append(now);
```

**스택에 들어있는 문자열들을 문자열로 변환한다.**

```java
StringBuilder ans = new StringBuilder();
for (String s : stack) {
    ans.append("/").append(s);
}
```

**스택이 비어있다면 '/'를 반환한다.**

```java
return ans.length() == 0 ? "/" : ans.toString();
```