# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        d1 = tmp = ListNode(-1)
        d2 = result = ListNode(-1)
        
        
        while(head):
            if(head.val < x):
                result.next = ListNode(head.val)
                result = result.next
            else:
                tmp.next = ListNode(head.val)
                tmp = tmp.next
            head = head.next
        result.next = d1.next
        return d2.next