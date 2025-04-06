# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # T: O(n), S: O(1) - Floyd's Tortoise and Hare algorithm
        # Phase 1: Detect cycle using slow/fast pointers
        # Phase 2: Find cycle start - when slow and fast meet again
        # Note: There can't be a cycle without tail node pointing somewhere
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:  # Cycle detected
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow  # Node where cycle begins
        return None  # No cycle