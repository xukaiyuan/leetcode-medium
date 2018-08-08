class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        length = len(board)
        width = len(board[0])

        status = [[0] * width for i in range(length)]

        for i in range(length):
            for j in range(width):
                neighbours = self.findNeighbours(board, i, j)
                lives = sum(neighbours)

                if(board[i][j] == 1):
                    if(lives == 2 or lives == 3):
                        status[i][j] = 1
                    else:
                        status[i][j] = 0
                else:
                    if(lives == 3):
                        status[i][j] = 1

        for i in range(length):
            for j in range(width):
                board[i][j] = status[i][j]


    def findNeighbours(self, board, i, j):
        neighbours = []
        if(i -1 >= 0):
            neighbours.append(board[i - 1][j])
            if(j - 1 >= 0):
                neighbours.append(board[i - 1][j - 1])
            if(j + 1 <= len(board[0]) - 1):
                neighbours.append(board[i - 1][j + 1])
        if(i + 1 <= len(board) - 1):
            neighbours.append(board[i + 1][j])
            if(j + 1 <= len(board[0]) - 1):
                neighbours.append(board[i + 1][j + 1])
            if(j - 1 >= 0):
                neighbours.append(board[i + 1][j - 1])

        if(j - 1 >= 0):
            neighbours.append(board[i][j - 1])
        if(j + 1 <= len(board[0]) - 1):
            neighbours.append(board[i][j + 1])

        return neighbours