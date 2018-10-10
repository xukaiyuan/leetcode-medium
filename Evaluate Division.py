class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        id = []
        relation = {}
        count = 0
        res = []
        weight = []
        
        def find(p):
            if(p == id[p]):
                return p
            root = find(id[p])
            weight[p] *= weight[id[p]]
            id[p] = root
            return root
        
        def connected(p, q):
            return find(p) == find(q)
        
        def union(p, q, val):
            index_p = find(p)
            index_q = find(q)
            
            if(not connected(p, q)):
                id[index_p] = index_q
                weight[index_p] = val * weight[q] / weight[p] 
        
        for i in equations:
            index = equations.index(i)
            if(i[0] not in relation):
                relation[i[0]] = count
                count += 1
                id.append(relation[i[0]]) 
                weight.append(1.0)
            if(i[1] not in relation):
                relation[i[1]] = count
                count += 1
                id.append(relation[i[1]])
                weight.append(1.0)
            union(relation[i[0]], relation[i[1]], values[index])
            
        for i in queries:
            if(i[0] not in relation or i[1] not in relation or not connected(relation[i[0]], relation[i[1]])):
                res.append(-1.0)
            else:
                res.append(weight[relation[i[0]]] / weight[relation[i[1]]])
            
        
        return res