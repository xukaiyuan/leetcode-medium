# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if(root == None):
            return res
        q = Queue()
        q.put(root)

        while(not q.empty()):
            row = []
            size = q.qsize()
            for i in range(size):
                tmp = q.get()
                if(tmp.left != None):
                    q.put(tmp.left)
                if(tmp.right != None):
                    q.put(tmp.right)
                row.append(tmp.val)
            res.append(row)
        return res
