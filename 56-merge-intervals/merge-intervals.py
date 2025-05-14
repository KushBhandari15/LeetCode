class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        i = 1
        size = len(intervals)

        res = []
        if (size < 2):
            return intervals
        
        intervals.sort()
        prev = intervals[0]

        while (i < size):
            
            curr = intervals[i]
            prevEnd = prev[1]
            currStart = curr[0]

            if (prevEnd >= currStart):
                prev[0] = min(curr[0], prev[0])
                prev[1] = max(curr[1], prev[1])
            
            else:
                res.append(prev)
                prev = curr
            
            i += 1

        res.append(prev)
        
        return res