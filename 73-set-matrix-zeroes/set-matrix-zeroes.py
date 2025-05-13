class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        row = len(matrix)
        col = len(matrix[0])

        helperR = set()
        helperC = set()
        for i in range(row):
            for j in range(col):

                if (matrix [i][j] != 0):
                    continue

                helperR.add(i)
                helperC.add(j)
            
        
        for i in range (row):
            for j in range(col):
                if (i in helperR) or (j in helperC):
                    matrix[i][j] = 0
        
        return matrix
        