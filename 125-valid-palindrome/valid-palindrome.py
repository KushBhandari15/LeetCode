class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        string = ""
        for i in range (len(s)):
            
            if (s[i].isalnum()):

                string += s[i].lower()
            
        if (string == string[::-1]):
            return True

        return False
            