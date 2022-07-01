class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        for p in path.split("/"):
            if p == "..":
                if result:
                    result.pop()
            elif p == "." or p == "": continue
            else:
                result.append(p)
        return "/" + "/".join(result)

a = Solution()
print(a.simplifyPath("/../"))