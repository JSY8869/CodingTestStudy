# https://leetcode.com/problems/word-ladder-ii/


###################시간 초과###################
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        def check(word):
            tmp = []
            for i in range(N):
                cnt = 0
                if not used[i]:
                    for j in range(l):
                        if word[j] == wordList[i][j]:
                            cnt += 1
                    if cnt == l - 1:
                        tmp.append(wordList[i])
            
            return tmp
        
        def backtracking(word, res):
            if word == endWord:
                ans.append(res)
                return
            
            next_wordList = check(word)
            
            for next_word in next_wordList:
                used[wordList.index(next_word)] = True
                backtracking(next_word, res + [next_word])
                used[wordList.index(next_word)] = False
            
        N = len(wordList)
        l = len(beginWord)
        used = [False] * N
        ans = []
        _ans = []
        
        backtracking(beginWord, [beginWord])
        
        m = 1001
        for list in ans:
            m = min(len(list), m)
        
        for list in ans:
            if len(list) == m:
                _ans.append(list)
                
        return _ans
    
a = Solution()
print(a.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))


#################솔루션###################

from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        # BFS visit
        curr_level = {beginWord}        #bfs로 현재 탐색해야 하는 단어
        parents = defaultdict(list)     #해당 단어와 인접한 단어를 담아주는 딕셔너리
        while curr_level:
            wordList -= curr_level
            next_level = set()
            for word in curr_level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordList:
                            next_level.add(new_word)
                            parents[new_word].append(word)
            if endWord in next_level:
                break
            curr_level = next_level
        # DFS reconstruction
        res = []
        def dfs(word, path):
            if word == beginWord:
                path.append(word)
                res.append(path[::-1])
            else:
                for p_word in parents[word]:
                    dfs(p_word, path + [word])
        dfs(endWord, [])
        return res