#https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder(self, matrix):
        res = []
        left, right, high, low = 0, len(matrix[0]) - 1, 0, len(matrix) - 1      #left -> 왼쪽 끝, right -> 오른쪽 끝, high -> 위쪽 끝, low -> 아래쪽 끝
        while True:
            for i in range(left, right + 1):
                res.append(matrix[high][i])
            high += 1
            if high > low:
                break
            for i in range(high, low + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[low][i])
            low -= 1
            if high > low:
                break
            for i in range(low, high - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        
        return res

a = Solution()
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))