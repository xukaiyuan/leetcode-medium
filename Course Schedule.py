class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for x, y in prerequisites:
            graph[x].append(y)

        for i in range(numCourses):
            if(not self.helper(graph, visited, i)):
                return False
        return True

    def helper(self, graph, visited, i):
        if(visited[i] == 1):
            return True
        if(visited[i] == -1):
            return False

        visited[i] = -1
        for j in graph[i]:
            if(not self.helper(graph, visited, j)):
                return False
        visited[i] = 1
        return True