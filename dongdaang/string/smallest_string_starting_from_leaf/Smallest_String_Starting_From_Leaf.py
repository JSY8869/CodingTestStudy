#https://leetcode.com/problems/smallest-string-starting-from-leaf/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, s):
            if not node.left and not node.right:
                res.append(chr(node.val + 97) + s)
                return
            if node.left:
                dfs(node.left, chr(node.val + 97) + s)
            if node.right:
                dfs(node.right, chr(node.val + 97) + s)
        
        res = []
        dfs(root, '')
        res.sort()
        
        return res[0]
    
a = Solution()
print(a.smallestFromLeaf([0,1,2,3,4,3,4]))