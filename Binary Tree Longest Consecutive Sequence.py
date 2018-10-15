class Solution:
    def longestConsecutive(self, root):
    	if(not root):
    		return 0

    	res = 0

    	def dfs(root, fatherValue, cur_len, res):
    		if(not root):
    			return 
    		if(root.val == fatherValue + 1):
    			cur_len += 1
    		else:
    			cur_len = 0
    		res = max(res, cur_len)

    		dfs(root.left, root.val, cur_len, res)
    		dfs(root.right, root.val, cur_len, res)

    	dfs(root, root.val, 0, res)
    	return res
