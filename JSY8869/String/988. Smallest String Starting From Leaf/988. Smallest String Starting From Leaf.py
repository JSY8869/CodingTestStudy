from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node,path):
            if not node: # null
                return

            path += str(chr(node.val + 97))

            if not node.left and not node.right:
                paths.append(path[::-1])
            else:
                dfs(node.left,path)
                dfs(node.right,path)


        paths = []

        dfs(root,"")

        return min(paths)
        

a = Solution()
print(a.smallestFromLeaf([2,2,1,None,1,0,None,0]))