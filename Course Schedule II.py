class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        
        for x, y in prerequisites:
            graph[x].append(y)
        res = []
        if(len(prerequisites) == 0):
            for i in range(numCourses):
                res.append(i)
            return res
        for i in range(numCourses):
            if(len(graph[i]) == 0):
                continue
            if(not self.helper(graph, visited, i, res)):
                return []
            
        for i in range(numCourses):
            if(visited[i] == 0):
                res.append(i)
        return res



    def helper(self, graph, visited, i, res):
        if(visited[i] == 1):
            #res.append(i)
            return True
        if(visited[i] == -1):
            return False

        visited[i] = -1
        for j in graph[i]:
            if(not self.helper(graph, visited, j, res)):
                return False
        visited[i] = 1
        res.append(i)
        return True