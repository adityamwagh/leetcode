# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases (like removing the head)
        dummy = ListNode(0)
        dummy.next = head
        
        # Count the total number of nodes
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Find the node before the one to be removed
        position = length - n
        curr = dummy
        for i in range(position):
            curr = curr.next
        
        # Remove the target node
        curr.next = curr.next.next
        
        return dummy.next