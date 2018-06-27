# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if(len(postorder) == 0):
            return None
        inorder_dict = {}
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i

        size = len(postorder)
        return self.build(inorder, 0, size - 1, postorder, 0, size - 1, inorder_dict)

    def build(self, inorder, in_sta, in_end, postorder, pos_sta, pos_end, inorder_dict):
        if(in_sta > in_end or pos_sta > pos_end):
            return None

        root_index = inorder_dict[postorder[pos_end]]
        root = TreeNode(postorder[pos_end])
        gap = root_index - in_sta

        root.left = self.build(inorder, in_sta, root_index - 1, postorder, pos_sta, pos_sta + gap - 1, inorder_dict)
        root.right = self.build(inorder_dict, root_index + 1, in_end, postorder, pos_sta + gap, pos_end - 1, inorder_dict)

        return root
