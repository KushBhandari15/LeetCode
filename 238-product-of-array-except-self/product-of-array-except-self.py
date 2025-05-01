class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        size = len(nums)
        res = [1] * size
        res[0] = 1

        prefix = 1
        for i in range (size):
            prefix = prefix * nums[i]
            if (i != size-1):
                res[i+1] = prefix
        
        postfix = 1
        for j in range (size-1, -1, -1):
            postfix = postfix * nums[j]

            if (j != 0):
                res[j-1] = res[j-1] * postfix
        
        return res


            
        