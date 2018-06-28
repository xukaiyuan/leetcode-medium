# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if(root == None):
            return

        lst = []
        self.preorder(root, lst)
        root.val = lst[0]
        for i in range(1, len(lst)):
            new = TreeNode(lst[i])
            root.left = None
            root.right = new
            root = root.right
    
    def preorder(self, root, lst):
        if(root == None):
            return
        lst.append(root.val)
        self.preorder(root.left, lst)
        self.preorder(root.right, lst)

    	
