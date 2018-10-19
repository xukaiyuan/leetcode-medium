class solution:
	def hasPath(self, maze, start, destination):
		# maze: List[List[int]]
		# start: List[int]
		# end: List[int]
		# rtype: boolean
		if(len(maze) == 0 or len(maze[0]) == 0 or len(start) == 0 or len(destination) == 0):
			return False
		visited = [[0] * len(maze[0]) for _ in len(maze)]

		return self.dfs(maze, visited, start, destination)


	def dfs(self, maze, visited, start, destination):
		if(start == destination):
			return True
		if(visited[start[0]][start[1]]):
			return False

		visited[start[0]][start[1]] = 1

		direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

		for i in range(4):
			next_x = start[0]
			next_y = start[1]
			while(next_x > -1 and next_x < len(maze) and next_y > -1 and next_y < len(maze[0]) and maze[next_x][next_y] == 0):
				next_x += direction[i][0]
				next_y += direction[i][1]
			if(self.dfs(maze, visited, [next_x, next_y], destination)):
				return True
		return False
		