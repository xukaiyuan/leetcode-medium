# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        sort = []
        self.inOrder(root, sort)
        return sort[k - 1]

    def inOrder(self, root, sort):
        if(root.left == None and root.right == None):
            sort.append(root.val)
            return
        if(root.left):
            self.inOrder(root.left, sort)
        sort.append(root.val)
        if(root.right):
            self.inOrder(root.right, sort)