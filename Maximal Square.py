class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        length = len(matrix)
        if(length == 0):
            return 0
        width = len(matrix[0])
        max_length = 0
        dp = [([0] * width) for i in range(length)]
        
        for i in range(length):
            dp[i][0] = int((matrix[i][0] == "1"))
            max_length = max(max_length, dp[i][0])

        for j in range(width):
            dp[0][j] = int((matrix[0][j] == "1"))
            max_length = max(max_length, dp[0][j])

        for i in range(1, length):
            for j in range(1, width): 
                dp[i][j] = (min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1) * int((matrix[i][j] == "1"))
                max_length = max(max_length, dp[i][j])
                
        return max_length ** 2