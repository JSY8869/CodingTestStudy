# 1535. Find the Winner of an Array Game
## 문제 설명
- arr의 0번째 값과 1번째 값을 매번 비교한다.
- 둘 중 더 큰 값이 승리한다.
- 패배한 값은 맨 뒤로 옮긴다.
- 가장 먼저 k번 우승한 번호를 반환하라.
## 풀이
```python
# time limit....
from collections import defaultdict

class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = defaultdict()
        for value in arr:
            count[value] = 0
        while True:
            if arr[0] > arr[1]:
                count[arr[0]] += 1
                arr.append(arr.pop(1))
            else:
                arr.append(arr.pop(0))
                count[arr[0]] += 1
            if count[arr[0]] == k:
                return arr[0]
```

- 그냥 하나씩 비교하면서 작은값 뒤로 보냄
- k번 1등하면 반환
- **0번째 값이 최대값인 경우 더 돌 필요 없이 반환**