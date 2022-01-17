## 처음 코드
- 우선 순위의 문제 발생
- 더 많은 알파벳을 더 활용할 필요가 있음을 깨달음
```
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import deque
        q = deque()
        s = list(s)
        s.sort(reverse=True)
        q.append(s.pop(0))
        for _ in range(len(s)):
            length = len(q)
            for c in s:
                pp = q.pop()
                if pp == c:
                    q.append(pp)
                else:
                    q.append(pp)
                    q.append(c)
                    s.remove(c)
                    break
            if len(q) == length:
                return ""
        return "".join(q)
```
## 두 번째 코드
- 아니 이게 왜??
- vscode에서는 맞게 나오는데 제출하면 다르게 나옴;;
- "vvvlo" 넣어볼것
```
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        count = Counter(s)
        key = list(count.keys())
        value = list(count.values())
        result = []
        result.append(key[0])
        value[0] -= 1

        j = 0
        i = 0
        while i < len(key):
            if result[j] != key[i]:
                result.append(key[i])
                value[i] -= 1
                j += 1
                if value[i] == 0:
                    key.remove(key[i])
                    value.remove(value[i])
                i = -1
            i += 1
            
        if len(result) != len(s):
            return ""
        return "".join(result)
```

## 세 번째 코드
- 그냥 앞에서부터 정렬해가니 마지막에 남은걸 정렬하지 못해 오류 발생
```
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = sorted(sorted(s), key=s.count, reverse=True)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                for j in range(i+2, len(s)):
                    if s[i+1] != s[j]:
                        s[i+1], s[j] = s[j], s[i+1]
                if s[i] == s[i+1]:
                    return ""

        return "".join(s)
```