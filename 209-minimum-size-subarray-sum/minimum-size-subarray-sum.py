class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        

        res = float('inf')


        total_sum = 0
        start = 0
        
        for end in range (len(nums)):
            
            total_sum += nums[end]

            while (total_sum >= target):

                res = min(res, end-start+1)
                total_sum -= nums[start]
                start += 1
            
        
        return 0 if res == float('inf') else res