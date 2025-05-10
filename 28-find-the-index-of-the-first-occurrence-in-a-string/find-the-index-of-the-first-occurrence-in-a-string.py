class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        
        size = len(haystack)

        for i in range(size):
            count = 0
            temp = i
            while temp < size:
                if (haystack[temp] == needle[count]):
                    count += 1
                    temp += 1
                else:
                    break
                
                if (count == len(needle)):
                    return i
        
        return -1