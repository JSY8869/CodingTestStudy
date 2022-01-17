class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        import heapq
        n, counter = len(s), Counter(s)
        pq = [(-count, char) for char, count in counter.items()] # heapq 형식으로 바꾸면 최소값이 0번째 요소가 되기 때문에 음수로 바꿔 사용
        heapq.heapify(pq) # heapq형식으로 바꿔서 list로 반환
        maxOccur = -1*pq[0][0]

        if maxOccur > (n + 1) // 2: # 가장 많은 빈도수의 값이 반 이상인 경우 생성 불가
            return ""

        string = [''] * n
        i = 0
        while pq: # 그냥 2칸씩 번갈아가며 배치하고 끝
            count, char = heapq.heappop(pq)
            count *= -1
            for _ in range(count):
                string[i] = char
                i += 2
                if i >= n:
                    i = 1
        return "".join(string)
        

            


        


d = Solution()
print(d.reorganizeString("zrhmhyevkojpsegvwolkpystdnkyhcjrdvqtyhucxdcwm"))