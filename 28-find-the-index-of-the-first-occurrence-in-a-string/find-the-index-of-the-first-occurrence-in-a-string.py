class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        
        size = len(haystack)

        if (haystack == needle):
            return 0
        
        for i in range(size):
            count = 0
            temp = i + len(needle)

            print(i, " ", temp)
            if (haystack[i:temp] == needle):
                return i

        return -1