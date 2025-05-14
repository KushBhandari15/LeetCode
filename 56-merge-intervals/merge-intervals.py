class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        size = len(intervals)
        if (size < 2):
            return intervals
        
        res = []
        intervals.sort()
        i = 1

        while (i < size):
            

            if (intervals[i-1][1] >= intervals[i][0]):
                intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
            
            else:
                res.append(intervals[i-1])
            
            i += 1

        res.append(intervals[i-1])
        
        return res