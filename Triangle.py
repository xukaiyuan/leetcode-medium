# time limit exceed
class Solution:
    def dfs(self, cur_level, dis, minPath, triangle, cur_pos):
        if(cur_level == len(triangle)): 
            
            if(minPath[0] > dis):           
                minPath[0] = dis                 
            return
        
        start = max(cur_pos - 1, 0)
        end = min(cur_pos + 1, len(triangle[cur_level])) + 1
        
        self.dfs(cur_level + 1, dis + triangle[cur_level][cur_pos], minPath, triangle, cur_pos)
        self.dfs(cur_level + 1, dis + triangle[cur_level][cur_pos], minPath, triangle, cur_pos + 1)
        
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        minPath = [float('inf')]
        self.dfs(0, 0, minPath, triangle, 0)
        return minPath[0]

# Accepted
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if(len(triangle) == 0):
            return 0
        if(len(triangle) == 1):
            return triangle[0][0]
        path = [float('inf')] * len(triangle)

        for i in range(len(triangle[-1])):
            path[i] = triangle[-1][i]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(0, len(triangle[i + 1]) - 1):
                path[j] = triangle[i][j] + min(path[j], path[j + 1])

        return path[0]

