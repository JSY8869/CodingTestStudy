## Greedy - [Video Stitching](https://leetcode.com/problems/video-stitching/)

### 문제설명

- 시작시간과 끝나는시간이 있는 비디오 클립들이 존재한다.
- 각각의 비디오 클립은 시간이 겹칠수도 있고, 런타임시간이 다양하다.

각각의 비디오 클립들을 쪼개거나 그대로 붙여서 0~time까지의 원본의 비디오 클립을 완성하는데, 몇개의 세그먼드로 구성되는지
최소값을 구하여라. 단, 구성할 수 없으면 -1을 반환한다.

### 문제풀이

- 문제풀이 전략
    - 정렬
    - 스케줄링
    - 그리디

- 문제풀이 설명
  - 클립 배열을 시작시간을 기준으로 오름차순 정렬하고, 같으면 끝나는 시간을 기준으로 내림차순 정렬한다.

**필터링**

시작시간을 기준으로 오름차순 정렬을 했으므로, 시작시간이 0초부터 시작하지 않으면 -1을 반환한다.

```java
if(clips[0][0] != 0) return -1;
```

**변수 설정**

시작 세그먼트를 1로 두고, 0번째 세그먼트는 시작시간과 끝나는시간이 각각 0이라고 가정한다. 또한 편집된 비디오 배열을 만들어서
시작시간과 끝나는시간을 업데이트한다.

```java
int segment = 1;
int[][] editedVideo = new int[clips.length+1][2];
```

**동작**

```java
    for(int[]clip:clips){
        // TODO : 다음 편집점이 필요하다면 -> 현재 클립이 전 클립과 이어지지 않고 끝나는 시간이 더 뒤에 끝난다면
        if(editedVideo[segment-1][1]<clip[0]&&editedVideo[segment][1]<clip[1])segment++;
        // TODO : 전의 편집점과 이어지고, 더 늦게 끝나는 편집점이라면 -> 세그먼트 업데이트
        if(clip[1]>editedVideo[segment][1]){
        editedVideo[segment][0]=clip[0];
        editedVideo[segment][1]=clip[1];
        }

        // TODO : 런타임 시간이 이어지지 않는다면 종료
        if(editedVideo[segment-1][1]<editedVideo[segment][0])return-1;

        // TODO : 편집 중간에 이미 원하는 시간만큼의 비디오 클립을 완성했다면 종료
        if(editedVideo[segment][1]>=time)return segment;
    }
```