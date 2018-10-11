"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    
    def numIslands2(self, n, m, operators):
        # write your code here
        id = []
        self.count = 0
        grid = [[0] * m for _ in range(n)]
        res = []


        def find(p):
            if(p == id[p]):
                return p
            tmp = find(id[p])
            id[p] = tmp
            return tmp 
        
        def connected(p, q):
            return find(p) == find(q)
        
        def union(p, q):
            index_p = find(p)
            index_q = find(q)
            
            if(not connected(p, q)):
                id[index_p] = index_q
                self.count -= 1
        
        def valid(i, j):
            return i > -1 and i < n and j > -1 and j < m
        
        id = []
        for i in range(n):
            for j in range(m):
                id.append(i * m + j)
                
        
        for i in range(len(operators)):
            x, y = operators[i].x, operators[i].y
            if(grid[x][y] == 0):
                grid[x][y] = 1
                self.count += 1
                if(valid(x - 1, y) and grid[x - 1][y] != 0):
                    union(id[x * m + y], id[(x - 1) * m + y])
                if(valid(x + 1, y) and grid[x + 1][y] != 0):
                    union(id[x * m + y], id[(x + 1) * m + y])
                if(valid(x, y - 1) and grid[x][y - 1] != 0):
                    union(id[x * m + y], id[x * m + y - 1])
                if(valid(x, y + 1) and grid[x][y + 1] != 0):
                    union(id[x * m + y], id[x * m + y + 1])
            res.append(self.count)

        return res