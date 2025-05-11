class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l, r = 0, len(height)-1

        maxA = 0
        while (l < r):
            
            currentH = min(height[l], height[r])
            maxA = max(maxA, (currentH * (r-l)))

            if (height[l] < height[r]):
                l += 1
            
            else:
                r -= 1
        

        return maxA


        