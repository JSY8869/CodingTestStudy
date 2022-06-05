# https://leetcode.com/problems/find-the-winner-of-an-array-game/


from collections import defaultdict

class Solution:
    def getWinner(self, arr, k):
        win_cnt = defaultdict(int)      #각 숫자들의 승리 횟수를 저장하는 딕셔너리
        winner = 0
        
        if k >= len(arr):
            return max(arr)
        
        while True:
            p1, p2 = arr[0], arr[1]
            
            if p1 > p2:
                win_cnt[p1] += 1
                if win_cnt[p1] == k:
                    winner = p1
                    break
                else:
                    arr.pop(1)
                    arr.append(p2)
                    continue
            else:
                win_cnt[p2] += 1
                if win_cnt[p2] == k:
                    winner = p2
                    break
                else:
                    arr.pop(0)
                    arr.append(p1)
        
        return winner

a = Solution()
print(a.getWinner([3,2,1], 10))



##############Good Solution#############

def getWinner(self, A, k):
    cur = A[0]
    win = 0
    for i in range(1, len(A)):
        if A[i] > cur:
            cur = A[i]
            win = 0
        win += 1
        if (win == k): break
    return cur