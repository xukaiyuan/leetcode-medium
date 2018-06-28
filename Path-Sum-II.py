# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        
        if(root == None):
            return res
        self.findPath(root, sum, res, [])
        return res

    def findPath(self, root, sum, res, tmp):
        if(root == None):          
            return
        
        if(root.left == None and root.right == None):
            if(root.val == sum):
                tmp.append(root.val) 
                res.append(tmp)              
                return
        else:
            tmp.append(root.val) 
            tmp1 = tmp[:]
            tmp2 = tmp[:]
            self.findPath(root.left, sum - root.val, res, tmp1)     
            self.findPath(root.right, sum - root.val, res, tmp2)

