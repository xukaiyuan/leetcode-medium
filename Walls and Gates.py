import math
def wallAndGate(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if(grid[i][j] == 0):
				dfs(grid, i, j, 0)

	return grid


def dfs(grid, i, j, dis):
	if(i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] < dis):
		return
	grid[i][j] = dis
	dfs(grid, i + 1, j, dis + 1)
	dfs(grid, i, j + 1, dis + 1)
	dfs(grid, i - 1, j, dis + 1)
	dfs(grid, i, j - 1, dis + 1)


grid = [[math.inf, -1, 0, math.inf], [math.inf, math.inf, math.inf, -1], [math.inf, -1, math.inf, -1], [0, -1, math.inf, math.inf]]

res = wallAndGate(grid)
print(res)