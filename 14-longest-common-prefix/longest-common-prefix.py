class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        size = len(strs)
        res = 1000
        for i in range (1, size):
            count = 0
            current = strs[i]
            prev = strs[i-1]
            index = 0
            while index < len(current) and index < len(prev) and index < res:
                if (current[index] == prev[index]):
                    count += 1
                else:
                    break
                index += 1
            res = min(res, count)
        
        return strs[0][0:res]
