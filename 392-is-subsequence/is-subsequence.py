class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        p1 = 0

        if (len(s) == 0):
            return True

        for i in range(len(t)):

            if (s[p1] == t[i]):
                p1 += 1
                if (p1 == len(s)):
                    return True
            
        
        return False