class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        helper = {}


        for i in range(len(nums)):

            needed = target - nums[i]

            if needed in helper:
                return [i, helper[needed]]
            
            helper[nums[i]] = i
        
