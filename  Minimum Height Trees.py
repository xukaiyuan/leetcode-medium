class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if(n == 1):
            return [0]
        edge_dict = {}
        leaves = []
        for i in edges:
            if(i[0] in edge_dict):
                tmp = edge_dict[i[0]]
                tmp.append(i[1])
                edge_dict[i[0]] = tmp
            else:
                edge_dict[i[0]] = [i[1]]

            if(i[1] in edge_dict):
                tmp = edge_dict[i[1]]
                tmp.append(i[0])
                edge_dict[i[1]] = tmp
            else:
                edge_dict[i[1]] = [i[0]]

        for i in edge_dict:
            if(len(edge_dict[i]) == 1):
                leaves.append(i)

        while(n > 2):
            n -= len(leaves)
            tmp_leaves = []
            for leaf in leaves:
                father = edge_dict[leaf][0]
                tmp_children = edge_dict[father]
                tmp_children.remove(leaf)
                if(len(tmp_children) == 1):
                    tmp_leaves.append(father)
                edge_dict[father] = tmp_children
                del edge_dict[leaf]
            leaves = tmp_leaves[:]
        return leaves
