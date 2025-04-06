# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # T: O(n): S: O(1)
        # Find middle of linked-list
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Cut the link to middle element
        prev.next = None

        # Reverse the second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # Iterate over both and find max twin sum
        max_pair_sum = 0
        list1 = head
        list2 = prev
        
        while list1 and list2:
            max_pair_sum = max(max_pair_sum, list1.val + list2.val)
            list1 = list1.next
            list2 = list2.next
        
        return max_pair_sum
