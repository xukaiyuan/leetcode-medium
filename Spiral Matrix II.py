class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if(n == 0):
            return []
        res = [[0] * n for _ in range(n)]

        def dfs(res, i, j, count, n, direction):
            if(i < 0 or j < 0 or i > n - 1 or j > n - 1 or res[i][j] != 0):
                return

            res[i][j] = count

            if(direction == 1):
                dfs(res, i, j + 1, count + 1, n, 1)
                dfs(res, i + 1, j, count + 1, n, 2)
            elif(direction == 2):
                dfs(res, i + 1, j, count + 1, n, 2)
                dfs(res, i, j - 1, count + 1, n, 3)
            elif(direction == 3):
                dfs(res, i, j - 1, count + 1, n, 3)
                dfs(res, i - 1, j, count + 1, n, 4)
            elif(direction == 4):
                dfs(res, i - 1, j, count + 1, n, 4)
                dfs(res, i, j + 1, count + 1, n, 1)

        dfs(res, 0, 0, 1, n, 1)
        return res