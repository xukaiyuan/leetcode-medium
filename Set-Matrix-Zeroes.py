class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if(j == 0):
                    if(matrix[i][j] == 0):
                        col0 = 0
                elif(matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if(j == 0):
                    break
                if(matrix[i][0] == 0 or matrix[0][j] == 0):
                	matrix[i][j] = 0
        if(col0 == 0):
            for t in range(rows):
                matrix[t][0] = 0
