class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        


        res = []

        row = len(matrix)
        col = len(matrix[0])

        rStep = 0
        cStep = 1
        x, y = 0, 0
        
        for i in range (row*col):

            res.append(matrix[x][y])
            matrix[x][y] = -101
            
            if (not (x+rStep >= 0 and x+rStep < row and y+cStep >= 0 and y+cStep < col) or matrix[x+rStep][y+cStep] == -101):
                
                temp = cStep
                cStep = -rStep
                rStep = temp

            x += rStep
            y += cStep

        return res