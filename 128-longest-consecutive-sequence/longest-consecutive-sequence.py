class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()

        if len(nums) == 0:
            return 0
        
        count = 1
        maxCount = 1
        for i in range (1, len(nums)):
            
            if (nums[i] == nums[i-1]+1):
                count += 1
            
            elif (nums[i] == nums[i-1]):
                continue
            
            else:
                count = 1

            maxCount = max(maxCount, count)
        

        return maxCount