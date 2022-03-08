#https://leetcode.com/problems/sort-characters-by-frequency/



#####################Counter 사용 풀이####################
from collections import Counter

class Solution:
    def frequencySort(self, s):
        ans = ''
        letters = Counter(s)        #카운터 함수로 알파벳 개수를 세주기
        letters = sorted(letters.items(), reverse= True, key= lambda x : x[1])      #letters 딕셔너리를 value 값을 기준으로 내림차순 정렬
        for i in letters:
            ans += i[0] * i[1]      #해당 글자를 카운트된 횟수만큼 출력하기
        return ans
        
a = Solution()
print(a.frequencySort("tree"))


####################Counter 사용 안한 풀이################
class Solution:
    def frequencySort(self, s):
        letters = {}
        ans = ''
        for c in s:                 #카운트 함수를 대신해 직접 카운트 해서 딕셔너리에 저장
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1
        letters = sorted(letters.items(), reverse= True, key= lambda x : x[1])
        for i in letters:
            ans += i[0] * i[1]
        return ans