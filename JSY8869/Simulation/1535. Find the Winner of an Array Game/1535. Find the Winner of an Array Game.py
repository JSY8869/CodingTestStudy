
from collections import defaultdict


class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = defaultdict()
        max_value = max(arr)
        for value in arr:
            count[value] = 0
        while True:
            if arr[0] > arr[1]:
                count[arr[0]] += 1
                arr.append(arr.pop(1))
            else:
                arr.append(arr.pop(0))
                count[arr[0]] += 1
            if count[arr[0]] == k or count[arr[0]] == max_value:
                return arr[0]




a = Solution()
print(a.getWinner([2,1,3,5,4,6,7],2))