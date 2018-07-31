class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j):
            if(i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != "1" ):
                return
            grid[i][j] = "*"
            dfs(grid, i , j + 1)
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)

        if(len(grid) == 0):
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    dfs(grid, i, j)
                    count += 1
        return count
        