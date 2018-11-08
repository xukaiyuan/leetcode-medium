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
            next_x -= direction[i][0]
            next_y -= direction[i][1]
			if(self.dfs(maze, visited, [next_x, next_y], destination)):
				return True
		return False

import java.util.Arrays;
public class Solution {
    /**
     * @param maze: the maze
     * @param start: the start
     * @param destination: the destination
     * @return: whether the ball could stop at the destination
     */
    private int[][] visited;
    private int[][] direction = {{0, 1}, {0, -1}, {1, 0}, {1, -1}};
    private int row;
    private int col;
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        // write your code here
        if(maze.length == 0 || maze[0].length == 0 || start.length == 0 || destination.length == 0) {
            return false;
        }
        row = maze.length;
        col = maze[0].length;
        visited = new int[row][col];
        
        return dfs(maze, start, destination);
    }
    
    public boolean dfs(int[][] maze, int[] start, int[] destination) {
        if(Arrays.equals(start, destination)) {
            return true;
        }

        if(visited[start[0]][start[1]] == 1) {
            return false;
        }
        visited[start[0]][start[1]] = 1;
        for (int i = 0; i < 4; i++) {
            int x = start[0];
            int y = start[1];
            while(x > -1 && x < row && y > -1 && y < col && maze[x][y] == 0) {
                x += direction[i][0];
                y += direction[i][1];
            }
            
            x -= direction[i][0];
            y -= direction[i][1];
            
            int[] startNew = {x, y};
            if(dfs(maze, startNew, destination)) {
                return true;
            }
        }
        return false;
        
    }
}

maze II

class Solution {
public:
    vector<vector<int>> dirs{{0,-1},{-1,0},{0,1},{1,0}};
    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int m = maze.size(), n = maze[0].size();
        vector<vector<int>> dists(m, vector<int>(n, INT_MAX));
        dists[start[0]][start[1]] = 0;
        helper(maze, start[0], start[1], destination, dists);
        int res = dists[destination[0]][destination[1]];
        return (res == INT_MAX) ? -1 : res;
    }
    void helper(vector<vector<int>>& maze, int i, int j, vector<int>& destination, vector<vector<int>>& dists) {
        if (i == destination[0] && j == destination[1]) return;
        int m = maze.size(), n = maze[0].size();
        for (auto d : dirs) {
            int x = i, y = j, dist = dists[x][y];
            while (x >= 0 && x < m && y >= 0 && y < n && maze[x][y] == 0) {
                x += d[0];
                y += d[1];
                ++dist;
            }
            x -= d[0];
            y -= d[1];
            --dist;
            if (dists[x][y] > dist) {
                dists[x][y] = dist;
                helper(maze, x, y, destination, dists);
            }
        }
    }
};
		