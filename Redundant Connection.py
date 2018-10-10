class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        id = []
        res = [-1, -1]
        
        def find(p):
            if(p == id[p]):
                return p
            root = find(id[p])
            id[p] = root
            return root
        
        def connected(p, q):
            return id[p] == id[q]
        
        def union(p, q):
            index_p = find(p)
            index_q = find(q)
            
            if(not connected(p, q)):
                id[index_p] = index_q
                return False
            else:
                return True
        n = -1   
        for i in edges:
            n = max(n, i[0], i[1])
        
        for i in range(n):
            id.append(i)
        
        for i in edges:
            flag = union(i[0] - 1, i[1] - 1)
            if(flag):
                res = i[:]
        return res
                