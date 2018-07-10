class Solution:
    def search(self, board, i, j):
        if(i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or board[i][j] != 'O'):
            return
        board[i][j] = 'x'
        self.search(board, i + 1, j)
        self.search(board, i, j + 1)
        self.search(board, i, j - 1)
        self.search(board, i - 1, j)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if(len(board) == 0 or len(board[0]) == 0):
            return
        for i in range(len(board)):
            if(board[i][0] == 'O'):
                self.search(board, i, 0)
            if(board[i][len(board[0]) - 1] == 'O'):
                self.search(board, i, len(board[0]) - 1)

        for i in range(1, len(board[0]) - 1):
            if(board[0][i] == 'O'):
                self.search(board, 0, i)
            if(board[len(board) - 1][i] == 'O'):
                self.search(board, len(board) - 1, i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == 'O'):
                    board[i][j] = 'X'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == 'x'):
                    board[i][j] = 'O'

