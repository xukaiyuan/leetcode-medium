class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        if(len(row) == 0):
            return 0
        n = len(row)
        self.res = 0
        id = []
        for i in range(n):
            if(i % 2 == 0):
                id.append(i)
            else:
                id.append(i - 1)

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
                self.res += 1

        for i in range(0, n, 2):
            union(id[row[i]], id[row[i + 1]])

        return self.res