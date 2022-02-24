from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dictionary = dict()
        
        for i in s:
            if i not in dictionary:dictionary[i] = 1 # 없으면 1개로 지정
            else: dictionary[i] += 1 # 있으면 개수 +
        dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True) # 빈도수 정렬
        
        # 형태 맞춰주기
        result = []
        for a, b in dictionary:
            for _ in range(b):
                result.append(a)
        return "".join(result)

a = Solution()
print(a.frequencySort("Aabb"))