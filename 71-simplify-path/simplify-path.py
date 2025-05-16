class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stack = []
        for d in path.split('/'):
            if d == "..":
                if stack:
                    stack.pop()
            elif d and d != ".":
                stack.append(d)
        
        return "/" + "/".join(stack)