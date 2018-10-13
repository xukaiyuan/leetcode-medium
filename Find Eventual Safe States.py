class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # 0 as unvisited, 1 as entry, 2 as exit
        visited = [0] * len(graph)

        def dfs(graph, i):
            if(visited[i] != 0):
                return visited[i] == 2

            visited[i] = 1

            for nei in graph[i]:
                if(visited[nei] == 2):
                    continue
                if(visited[nei] == 1 or not dfs(graph, nei)):
                    return False

            visited[i] = 2
            return True

        res = []
        for i in range(len(graph)):
            if(dfs(graph, i)):
                res.append(i)

        return res