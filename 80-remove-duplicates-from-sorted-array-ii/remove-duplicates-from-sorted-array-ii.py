class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        j = 0
        count = 1
        for i in range (1, len(nums)):

            if (nums[j] != nums[i]):
                j += 1
                nums[j] = nums[i]
                count = 1
            
            else:
                if (count < 2):
                    j += 1
                    count += 1
                    nums[j] = nums[i]
                
        
        return j+1

        