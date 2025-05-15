class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        intervals.append(newInterval)

        intervals.sort()

        if len(intervals) == 0:
            return []
        i = 1
        res = []
        while (i < len(intervals)):

            if (intervals[i-1][1] >= intervals[i][0]):
                intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
            
            else:
                res.append(intervals[i-1])

            i += 1
        
        
        res.append(intervals[len(intervals)-1])

        return res

