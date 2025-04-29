class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        maximum = max(citations)
        res = 0
        for i in range (maximum+1):
            count = 0
            for j in citations:
                if (j >= i):
                    count += 1
            
            if (count >= i):
                res = max(i, res)
        
        return res

        