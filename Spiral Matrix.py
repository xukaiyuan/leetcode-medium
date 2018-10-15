class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        self.res = []

        # 1: right, 2: down, 3: left, 4: up

        def dfs(matrix, i, j, direction):
            if(i < 0 or j < 0 or i > len(matrix) - 1 or j > len(matrix[0]) - 1 or visited[i][j]):
                return
            self.res.append(matrix[i][j])
            visited[i][j] = 1

            if(direction == 1):
                dfs(matrix, i, j + 1, 1)
                dfs(matrix, i + 1, j, 2)
            elif(direction == 2):
                dfs(matrix, i + 1, j, 2)
                dfs(matrix, i, j - 1, 3)
            elif(direction == 3):
                dfs(matrix, i, j - 1, 3)
                dfs(matrix, i - 1, j, 4)
            else:
                dfs(matrix, i - 1, j, 4)
                dfs(matrix, i, j + 1, 1)

        dfs(matrix, 0, 0, 1)
        return self.res