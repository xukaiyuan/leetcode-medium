class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = []
        col = []
        square = []
        
        for i in range(9):
            tmp_row = set()
            tmp_col = set()
            tmp_sqr = set()
            row.append(tmp_row)
            col.append(tmp_col)
            square.append(tmp_sqr)
        
        for i in range(9):
            for j in range(9):
                if(board[i][j] != "."):
                    if(board[i][j] in row[i]):
                        return False
                    else:
                        row[i].add(board[i][j])
                        
                    if(board[i][j] in col[j]):
                        return False
                    else:
                        col[j].add(board[i][j])
                        
                    id_row = int(i / 3)
                    id_col = int(j / 3)
                    
                    id_square = id_row * 3 + id_col
                    
                    if(board[i][j] in square[id_square]):
                        return False
                    else:
                        square[id_square].add(board[i][j])
                        
        return True