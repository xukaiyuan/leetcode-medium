# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if(root != None):
        	res.append(root.val)
        return res

        def helper(res, root):
        	if(root.left == None and root.right == None):
        		return
        	elif(root.right != None):
        		root = root.right
        		
        	elif(root.left != None):
        		root = root.left

        	res.append(root.val)
        	helper(res, root)