# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# use list as a queue
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if(root == None):
            return res
        count = 0
        q = deque([])
        q.append(root)

        while(len(q) != 0):
            row = []
            size = len(q)
            for i in range(size):
                tmp = q.popleft()
                if(tmp.left != None):
                    q.append(tmp.left)
                if(tmp.right != None):
                    q.append(tmp.right)
                row.append(tmp.val)
            if(count % 2 == 1):
                row.reverse()
            count += 1
            res.append(row)
        return res
