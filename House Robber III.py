# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level traversal doesn't work
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        res = []
        level = self.levelOrder(root, res)
        print(res)
        
        if(level == 1):
            return root.val
        if(level == 2):
            return max(res[0], res[1] + res[2])
        dp = [0] * level
        dp[0] = root.val
        dp[1] = max(res[0], res[1] + res[2])
        for i in range(2, level):
            dp[i] = max(dp[i - 2] + sum(res[2 ** i - 1: 4 * 2 ** (i - 1) - 1]), dp[i - 1])
            
        #print(dp)
        return dp[-1]
    def levelOrder(self, root, res):
        if(root == None):
            return
        tmp = []
        tmp.append(root)
        level = 0
        while(len(tmp) != 0):
            level += 1
            size = len(tmp)
            cnt = 0
            while(cnt < size):
                root_tmp = tmp.pop(0)
                cnt += 1
                if(root_tmp != None):
                    res.append(root_tmp.val)
                else:
                    res.append(0)
                if(root_tmp != None and (root_tmp.left != None or root_tmp.right != None)):
                    if(root_tmp.left != None):
                        tmp.append(root_tmp.left)
                    else:
                        tmp.append(None)
                    if(root_tmp.right != None):
                        tmp.append(root_tmp.right)
                    else:
                        tmp.append(None)
            gap = 2 ** (level - 1) - size 
            for i in range(gap):
                res.append(0)
        return level


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        def dfs(node):
            if not node: return 0, 0
            l, r = dfs(node.left), dfs(node.right)
            return max(l) + max(r), node.val + l[0] + r[0]
        return max(dfs(root))
