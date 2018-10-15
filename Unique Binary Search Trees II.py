# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if(n == 0):
            return []
        return self.recursion(1, n)

    def recursion(self, start, end):
        subTree = []
        if(start > end):
            subTree.append(None)
            return subTree

        for i in range(start, end + 1):
            left = self.recursion(start, i - 1)
            right = self.recursion(i + 1, end)

            for l in left:
                for r in right:
                    tmp = TreeNode(i)
                    tmp.left = l
                    tmp.right = r
                    subTree.append(tmp)

        return subTree