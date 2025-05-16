class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for b in s:

            if (b == "(" or b =="{" or b == "["):
                stack.append(b)

            else:
                if not stack:
                    return False
                element = stack.pop()
                if b == ")" and element != "(":
                    return False
                elif b == "}" and element != "{":
                    return False
                elif b == "]" and element != "[":
                    return False

        if not stack:
            return True
        else:
            return False
        