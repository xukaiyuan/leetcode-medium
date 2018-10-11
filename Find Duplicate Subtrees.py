class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        record = {}

        def dfs(root, record, res):
            if(root == None):
                return "#"
            tmp = dfs(root.left, record, res) + dfs(root.right, record, res) + str(root.val)
            if(tmp in record and record[tmp] == 1):
                res.append(root)
            record[tmp] = record.get(tmp, 0) + 1
            return tmp

        dfs(root, record, res)


        return res