class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        helper = {}
        words = s.split()
        wordCount = set()

        if (len(words) != len(pattern)):
            return False
        for i in range(len(words)):
            
            if (pattern[i] not in helper):
                if (words[i] in wordCount):
                    return False
                helper[pattern[i]] = words[i]
                wordCount.add(words[i])
            if (helper[pattern[i]] != words[i]):
                return False
        

        return True
                