# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = [0]
        missRight = [0]
        if(root == None):
            return 0
        self.countLevel(root, level)
        self.traversal(root, missRight, 0, level)
        
        sum = 0
        for i in range(level[0] + 1):
            sum += 2 ** i
        
        return sum - missRight[0]

    def traversal(self, root, missRight, cur_level, level):
        if(root.left == None and root.right == None):
            if(cur_level != level[0]):
                missRight[0] += 2
            else:
                return
        elif(root.right == None):
            cur_level += 1
            missRight[0] += 1
            self.traversal(root.left, missRight, cur_level, level)
        else:
            cur_level += 1
            self.traversal(root.left, missRight, cur_level, level)
            self.traversal(root.right, missRight, cur_level, level)

    def countLevel(self, root, level):
        if(root.left == None):
            return
        else:
            level[0] += 1
            self.countLevel(root.left, level)

# ^the above one time exceeds in the last test case!

# this one is god like
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level_whole = self.countLevel(root, 0)
        if(level_whole < 0):
            return 0
        else:
            level_right = self.countLevel(root.right, 0)
        
            if(level_whole == (level_right + 1)):
                return 2 ** level_whole + self.countNodes(root.right)
            else:
                return 2 ** (level_whole - 1) + self.countNodes(root.left)  

    def countLevel(self, root, level):
        if(root == None):
            return -1
        while(root.left):
            root = root.left
            level += 1
        return level
            

        