# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
        	return head
        odd = head
        even = head.next
        even_head = even

        while(even != None and even.next != None):
        	odd.next = even.next
        	odd = odd.next
        	even.next = odd.next
        	even = even.next
        odd.next = even_head

        return head