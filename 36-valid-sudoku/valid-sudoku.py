class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        box = [[] for _ in range(9)]

        for i in range (9):
            for j in range (9):
                
                if (board[i][j] == "."):
                    continue
                
                boxNum = (3 * (i//3)) + j//3
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in box[boxNum]):
                    return False
                
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                box[boxNum].append(board[i][j])
                # print(rows)
                # print(cols)
                print(box)

        return True