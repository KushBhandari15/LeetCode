class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        res = []
        if not nums:
            return []
        start = 0
        for i in range (1, len(nums)):

            if (nums[i-1] + 1 != nums[i]):
                
                s = nums[start]
                e = nums[i-1]
                if (start != i-1):
                    res.append(str(s) + "->" + str(e))
                else:
                    res.append(str(s))

                start = i
            
        s = nums[start]
        e = nums[-1]
        if (start != len(nums)-1):
            res.append(str(s) + "->" + str(e))
        else:
            res.append(str(s))
        return res
