class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""

        size = len(s)
        i = size - 1

        current = ""
        while i >=0 :
            if (s[i] == " " and current):
                res += current[::-1] + " "
                current = ""
            else:
                current += s[i]
            
            i -= 1
        
        if current:
            res += current[::-1] + " "
        
        return ' '.join(res.strip().split())



        