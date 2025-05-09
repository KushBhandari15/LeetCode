class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        size = len(s)
        res = 0
        space = False
        for i in range(size):
            
            if s[i] == " ":
                space = True
            else:
                if (space == True):
                    res = 1
                else:
                    res += 1
                
                space = False
            
        return res