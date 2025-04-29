class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        size = len(citations)
        paper_count = [0] * (size+1)

        for i in citations:
            paper_count[min(size, i)] += 1
        

        h = size
        papers = paper_count[size]

        while (papers < h):
            h -= 1
            papers += paper_count[h]
        
        return h