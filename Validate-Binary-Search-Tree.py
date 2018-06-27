# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def inOrder(root, lst):
            if(root == None):
                return
            inOrder(root.left, lst)
            lst.append(root.val)
            inOrder(root.right, lst)
        
        lst = []
        inOrder(root, lst)
        for i in range(len(lst) - 1):
            if(lst[i] >= lst[i + 1]):
                return False
        return True
        
