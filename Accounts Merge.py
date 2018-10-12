class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        id = []
        emails = {}
        parent = {}
        name = {}
        idToName = []
        count = 0
        unioned = set()

        def find(p):
            if(p == id[p]):
                return p
            root = find(id[p])
            id[p] = root
            return root

        def connected(p, q):
            return find(p) == find(q)

        def union(p, q):
            index_p = find(p)
            index_q = find(q)

            if(not connected(p, q)):
                id[index_p] = index_q               


        for i in accounts:
            for j in range(1, len(i)):
                if(i[j] not in emails):
                    emails[i[j]] = count
                    idToName.append(i[j])
                    id.append(count)
                    count += 1


        for i in accounts:
            for j in range(1, len(i)):
                if(i[1] not in name):
                    name[i[1]] = i[0]
                union(emails[i[1]], emails[i[j]])
                unioned.add(i[j])
                if(i[1] not in unioned):
                    unioned.add[i[1]]
                    if(i[1] not in parent):
                        parent[i[1]] = set([emails[i[j]]])
                    else:
                        tmp = parent[i[1]]
                        tmp.add(emails[i[j]])
                        parent[i[1]] = tmp                  
                else:
                    root = -1
                    if(len(parent) == 0):
                        parent[i[1]] = set([emails[i[j]]])
                        
                    else:
                        for par in parent:
                            if(connected(emails[par], emails[i[1]])):
                                root = par
                                break
                        if(root != -1):
                            tmp = parent[root]
                            tmp.add(emails[i[j]])
                            parent[root] = tmp
                        else:
                            parent[i[1]] = set([emails[i[j]]])
    
        
        res = []
        for i in parent:
            tmp = []
            for j in parent[i]:
                tmp.append(idToName[j])
            tmp.sort()
            tmp = [name[i]] + tmp
            res.append(tmp)
        return res