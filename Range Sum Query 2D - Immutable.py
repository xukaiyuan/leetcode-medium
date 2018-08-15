class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return
        length = len(matrix)
        width = len(matrix[0])
        self.cache = [[0] * (width + 1) for i in range(length)]
        for i in range(length):
            for j in range(width):
                self.cache[i][j + 1] = self.cache[i][j] + matrix[i][j]



    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1, row2 + 1):
            res += self.cache[i][col2 + 1] - self.cache[i][col1]
        return res


    # Your NumMatrix object will be instantiated and called as such:
    # obj = NumMatrix(matrix)
    # param_1 = obj.sumRegion(row1,col1,row2,col2)