class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        if(board[click[0]][click[1]] == "M"):
            board[click[0]][click[1]] = "X"
            return board
        elif(board[click[0]][click[1]] == "E"):
            self.dfs(board, click[0], click[1])
        return board

    def countMine(self, board, i, j):
        cnt = 0
        for x in range(max(0, i - 1), min(i + 2, len(board))):
            for y in range(max(0, j - 1), min(j + 2, len(board[0]))):
                if(board[x][y] == "M"):
                    cnt += 1
        return cnt

    def dfs(self, board, i, j):
        if(i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1):
            return

        elif(board[i][j] == "B"):
            return

        count = self.countMine(board, i, j)

        if(count > 0):
            board[i][j] = str(count)
            return
        else:
            board[i][j] = "B"    	
            self.dfs(board, i, j + 1)
            self.dfs(board, i + 1, j)
            self.dfs(board, i - 1, j)
            self.dfs(board, i + 1, j + 1)
            self.dfs(board, i, j - 1)
            self.dfs(board, i - 1, j - 1)
            self.dfs(board, i - 1, j + 1)
            self.dfs(board, i + 1, j - 1)         