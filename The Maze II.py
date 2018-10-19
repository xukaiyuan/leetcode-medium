import sys
class solution:
	def hasPath(self, maze, start, destination):
		# maze: List[List[int]]
		# start: List[int]
		# end: List[int]
		# rtype: boolean
		if(len(maze) == 0 or len(maze[0]) == 0 or len(start) == 0 or len(destination) == 0):
			return False
		dist = [[sys.maxSize] * len(maze[0]) for _ in len(maze)]
		dist[0][0] = 0

		self.dfs(maze, dist, start)
		if(dist[destination[0]][destination[1]] == sys.maxSize):
			return -1
		else:
			dist[destination[0]][destination[1]]

	def compute(start, target):
		return abs(start[0] - target[0]) + abs(start[1] - target[1])

	def dfs(self, maze, dist, start):
		direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

		for i in range(4):
			next_x = start[0]
			next_y = start[1]
			while(next_x > -1 and next_x < len(maze) and next_y > -1 and next_y < len(maze[0]) and maze[next_x][next_y] == 0):
				next_x += direction[i][0]
				next_y += direction[i][1]
			if(dist[next_x][next_y] > dist[start[0]][start[1]] + self.compute(start, [next_x, next_y])):
				dist[next_x][next_y] = dist[start[0]][start[1]] + self.compute(start, [next_x, next_y])
				self.dfs(maze, dist, [next_x, next_y])
		
		