class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if (numRows == 1 or numRows > len(s)):
            return s

        rows = [""] * numRows
        currentRow = 0
        step = 1
        for i in range (len(s)):

            rows[currentRow] += s[i]

            if currentRow == 0:
                step = 1
            elif currentRow == numRows-1 :
                step = -1
            
            currentRow += step
        

        return ''.join(rows)

