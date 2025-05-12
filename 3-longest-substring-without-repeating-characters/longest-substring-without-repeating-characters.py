class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = 0
        helper = {}
        res = 0
        for end in range (len(s)):
            
            helper[s[end]] = helper.get(s[end], 0) + 1

            while (len(helper)  != (end-start+1)):

                helper[s[start]] -= 1
                if (helper[s[start]] <= 0):
                    del helper[s[start]]

                start += 1
            
            res = max(res, end-start+1)
        
        return res