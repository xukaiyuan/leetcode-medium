class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        length = len(edges)
        id = [0] * (length + 1)
        first = []
        second = []

        def find(p):
            if(p == id[p]):
                return p
            root = find(id[p])
            id[p] = root
            return root

        for edge in edges:
            if(id[edge[1]] == 0):
                id[edge[1]] = edge[0]
            else:
                first = [id[edge[1]], edge[1]]
                second = edge[:]
                edge[1] = 0

        for i in range(length + 1):
            id[i] = i

        for edge in edges:
            if(edge[1] == 0):
                continue
            p = find(edge[0])
            q = find(edge[1])

            if(p == q):
                if(len(first) == 0):
                    return edge
                else:
                    return first
            id[p] = q

        return second
