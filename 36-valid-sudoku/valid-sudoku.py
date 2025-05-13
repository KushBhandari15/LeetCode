class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range (9):
            for j in range (9):
                
                if (board[i][j] == "."):
                    continue
                
                boxNum = (3 * (i//3)) + j//3
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in box[boxNum]):
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                box[boxNum].add(board[i][j])
                # print(rows)
                # print(cols)
                print(box)

        return True