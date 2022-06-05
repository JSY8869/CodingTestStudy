from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(set)
        
        for word in wordList: # *를 제외하고 나머지 부분이 같은 단어끼리 묶음
            for i in range(len(word)):
                wild = word[:i] + '*' + word[i+1:]
                dic[wild].add(word)
                
        result = []
        
        q = deque()
        
        q.append((beginWord, [beginWord]))
        
        seen = set()
        
        while q:
            
            size = len(q)
            
            matched = []
            
            for i in range(size):
                word, path = q.popleft()
                
                if word == endWord:
                    result.append(path)
                    continue
                
                for i in range(len(word)): # 다음으로 올 수 있는 단어 조합
                    wild = word[:i] + '*' + word[i+1:]

                    for match in dic[wild]: # 단어 조합에 해당하는 단어들
                        if match not in seen:
                            q.append((match, path + [match])) # 현재 단어와 지금까지의 단어 조합
                            matched.append(match)
                            
            for match in matched: # 매치된 단어 예외에 추가
                seen.add(match)
                            
            if len(result) != 0: 
                return result
                        
        
        

    

a = Solution()
print(a.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))