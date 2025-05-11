class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l, r = 0, len(numbers)-1

        while l < r:

            left, right = numbers[l], numbers[r]

            if (left + right == target):
                return [l+1, r+1]
            
            elif(left + right < target):
                l += 1
            
            else:
                r -= 1

        
        return [0, 0]