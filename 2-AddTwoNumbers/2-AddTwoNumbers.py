            if node.val > 9: carry, node.val = 1, node.val%10
            else: carry = 0
        carry = 0
        while l1_node and l2_node:
            node.val = l1_node.val + l2_node.val + carry
        node = head = ListNode()
        l1_node, l2_node = l1, l2
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     def __init__(self, val=0, next=None):
#         self.val = val
# Definition for singly-linked list.
# class ListNode:
            node.next = ListNode()
            node = node.next
[
