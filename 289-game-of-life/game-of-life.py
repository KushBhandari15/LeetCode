class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        

        helper = set()

        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                count = 0
                #Up
                if (i-1 >= 0 and (board[i-1][j] == 1 or board[i-1][j] == -1)): count += 1
                #Down
                if (i+1 < row and (board[i+1][j] == 1 or board[i+1][j] == -1)): count += 1
                #Left
                if (j-1 >= 0 and (board[i][j-1] == 1 or board[i][j-1] == -1)): count += 1
                #Right
                if (j+1 < col and (board[i][j+1] == 1 or board[i][j+1] == -1)): count += 1
                #DiagonalL1
                if (i-1 >= 0 and j-1 >= 0 and (board[i-1][j-1] == 1 or board[i-1][j-1] == -1)): count += 1
                #DiagonalL2
                if (i+1 < row and j-1 >= 0 and (board[i+1][j-1] == 1 or board[i+1][j-1] == -1)): count += 1
                #DiagonalL3
                if (i-1 >= 0 and j+1 < col and (board[i-1][j+1] == 1 or board[i-1][j+1] == -1)): count += 1
                #DiagonalL4
                if (i+1 < row and j+1 < col and (board[i+1][j+1] == 1 or board[i+1][j+1] == -1)): count += 1

                if (count == 2):
                    pass
                elif (count == 3):
                    if (board[i][j] == 0):
                        board[i][j] = 2

                else:
                    if (board[i][j] == 1):
                        board[i][j] = -1     


        for i in range(row):
            for j in range(col):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
