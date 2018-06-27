# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if(head == None):
            return None
        if(head.next == None):
            return TreeNode(head.val)

        fast = head
        slow = head
        last = slow

        while(fast.next != None and fast.next.next != None):
            fast = fast.next.next
            last = slow
            slow = slow.next

        fast = slow.next
        last.next = None

        root = TreeNode(slow.val)

        if(head != slow):
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(fast)

        return root



