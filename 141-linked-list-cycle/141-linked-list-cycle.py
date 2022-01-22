# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # zero element linkedlist
        if head is None:
            return False
        
        # Single element linkedlist
        if head.next is None:
            return False
        
        # Iterate for max iterations
        for i in range(10000):
            if head.next is not None:
                head = head.next
        
        if head.next is not None:
            return True
        
        return False