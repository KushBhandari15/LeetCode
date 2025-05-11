class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l, r = 0, len(s) - 1

        while l < r:

            if (s[l].isalnum() == False):
                l += 1
            elif (s[r].isalnum() == False):
                r -= 1
            
            else:
                if (s[l].lower() == s[r].lower()):
                    l += 1
                    r -= 1
                else:
                    print(s[l], " ", s[r])
                    return False
        
        return True