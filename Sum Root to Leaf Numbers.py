# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findRoot(self, root, tmp, res):
        if(root.left == None and root.right == None):
            tmp += str(root.val)
            res.append(tmp)
            return
        else:
            tmp += str(root.val)
            if(root.left != None):
                self.findRoot(root.left, tmp, res)
            if(root.right != None):
                self.findRoot(root.right, tmp, res)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        tmp = ''
        res = []
        self.findRoot(root, tmp, res)
        res = list(map(int, res))
        return sum(res)