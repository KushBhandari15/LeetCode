class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        helper = set(nums)
        res = 0

        for i in helper:

            if i-1 in helper: continue

            j = 1

            while i + j in helper:
                j += 1
            
            res = max(res, j)
        
        return res

            