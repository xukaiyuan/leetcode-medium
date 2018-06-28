# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from queue import Queue
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if(root == None):
            return
        q = Queue()
        q.put(root)

        while(not q.empty()):
            size = q.size()
            pre = q.get()
            if(pre.left != None):
                q.put(pre.left)
            if(pre.right != None):
                q.put(pre.right)

            for i in range(size):
                if(i == 0):
                    continue
                cur = q.get()
                if(cur.left != None):
                    q.put(cur.left)
                if(cur.right != None):
                    q.put(cur.right)
                pre.right = cur
                pre = cur
            pre.right = None

