class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        nums.sort()
        for i in range (len(nums)):
            
            l, r = i + 1, len(nums) - 1
            if (i > 0  and nums[i] == nums[i-1]):
                continue 
            while l < r:
                
                if (nums[i] + nums[l] + nums[r] == 0):
                    temp = [nums[i], nums[l], nums[r]]
                    res.append(temp)
                    
                    while (l < r and nums[l] == nums[l+1]):
                        l += 1
                    
                    while (l < r and nums[r] == nums[r-1]):
                        r -= 1

                    l += 1
                    r -= 1
                elif (nums[i] + nums[l] + nums[r] > 0):
                    r -= 1
                
                else:
                    l += 1
        
        return res
        