class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        helper = {}

        for i in range (len(nums)):
            
            if nums[i] in helper:

                if (abs(helper[nums[i]] - i) <= k):
                    
                    return True

            
            helper[nums[i]] = i
        

        return False

            