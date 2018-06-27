# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inorder_dict = {}
        if(len(preorder) == 0):
            return None

        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i

        size = len(preorder)
        return self.build(preorder, 0, size - 1, inorder, 0, size - 1, inorder_dict)

    def build(self, preorder, pre_sta, pre_end, inorder, in_sta, in_end, inorder_dict):
        if(pre_sta > pre_end or in_sta > in_end):
            return None

        root_index = inorder_dict[preorder[pre_sta]]
        root = TreeNode(preorder[pre_sta])

        gap = root_index - in_sta

        root.left = self.build(preorder, pre_sta + 1, pre_sta + gap, inorder, in_sta, root_index - 1, inorder_dict)
        root.right = self.build(preorder, pre_sta + 1 + gap, pre_end, inorder, root_index + 1, in_end, inorder_dict)

        return root
