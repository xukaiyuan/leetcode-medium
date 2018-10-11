def maze(grid, start, end):
	# grid: 2D matrix
	# start: start [x1, y1]
	# end: end [x2, y2]

	visited = [[0] * len(grid) for _ in range(len(grid[0]))]
	dfs(grid, start[0], start[1], end[0], end[1], visited)
	return False

def dfs(grid, i, j, end_x, end_y, visited):
	dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
	if(i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == 1 or visited[i][j]):
		return
	if(i == end_x and j == end_y):
		return True
	visited[i][j] == 1
	for i in range(4):
		dfs(grid, i + dir[i][0], j + dir[i][1], end_x, end_y, visited)

grid = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1 ,0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]

res = maze(grid, [0, 4], [4, 4])
print(res)