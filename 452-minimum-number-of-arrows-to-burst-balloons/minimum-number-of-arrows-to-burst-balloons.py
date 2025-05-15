class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        if not points:
            return 0

        points.sort()
        res = 1
        compare = points[0][1]
        
        for i in range (1, len(points)):

            if (compare >= points[i][0]):
                compare = min(points[i][1], compare)
            
            else:
                res += 1
                compare = points[i][1]
        
    
        return res