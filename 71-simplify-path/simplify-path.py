class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        ref = path.split('/')
        print(ref)
        stack = []
        for d in ref:
            if not d or d == ".":
                continue
            elif d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        
        res = ""
        if not stack:
            return "/"
        else:
            for i in stack:
                res += "/" + i

        return res