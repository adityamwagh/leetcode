# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # T: O(log n): S: O(1)
        # Fast and slow pointers
        # Fast pointer moves twice as fast as slow.
        # When fast reaches the end, slow will be at the mid point
        slow, fast = head, head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next
        
        return slow