class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        p1, p2 = 0, 0

        if (len(s) == 0):
            return True
        while (p1 < len(s) and p2 < len(t)):

            if (s[p1] == t[p2]):
                p1 += 1
                if (p1 == len(s)):
                    return True
            
            p2 += 1
        
        return False