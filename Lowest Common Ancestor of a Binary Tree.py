# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if(not root or not p or not q):
        	return None
        relation = self.dfs(root)

        path_p = self.path(p, relation)
        path_q = self.path(q, relation)

        if(len(path_p) >= len(path_q)):
        	for i in path_q:
        		if(i in path_p):
        			return i
        else:
        	for i in path_p:
        		if(i in path_q):
        			return i

    def path(self, point, relation):
    	path = [point]
    	while(relation[point]):
    		path.append(relation[point])
    		point = relation[point]
    	return path

    def dfs(self, root):
    	relation = {root: None}

    	stack = [root]

    	while(stack):
    		cur = stack.pop()

    		if(cur.left):
    			stack.append(cur.left)
    			relation[cur.left] = cur
    		if(cur.right):
    			stack.append(cur.right)
    			relation[cur.right] = cur

    	return relation