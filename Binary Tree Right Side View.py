# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if(root == None):
        	return res
        q = queue.Queue()

        q.put(root)

        while(not q.empty()):
        	length = q.qsize()
        	right = False
        	while(length > 0):
        		tmp = q.get()
        		if(right == False):
        			right = True
        			res.append(tmp.val)
        		if(tmp.right != None):
        			q.put(tmp.right)
        		if(tmp.left != None):
        			q.put(tmp.left)

        		length -=1
        return res
