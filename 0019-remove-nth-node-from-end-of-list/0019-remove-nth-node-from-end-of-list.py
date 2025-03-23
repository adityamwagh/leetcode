# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head
        # This handles edge cases like removing the head node
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers to the dummy node
        slow, fast = dummy, dummy
        
        # Advance the fast pointer n+1 steps ahead
        # This creates a gap of n+1 between slow and fast
        for i in range(n+1):
            # If n is larger than the list length, fast will become None
            # But this shouldn't happen given the problem constraints
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        # When fast reaches the end, slow will be at the (n+1)th node from the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Skip the nth node from the end by updating the next pointer
        # slow.next is the node to remove, so we link to slow.next.next
        slow.next = slow.next.next
        
        # Return the head of the modified list
        # We use dummy.next instead of head in case head was removed
        return dummy.next