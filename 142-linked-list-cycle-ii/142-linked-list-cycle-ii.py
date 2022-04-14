# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            slow = head.next
            fast = head.next.next

            while slow != fast:
                slow = slow.next
                fast = fast.next.next

            fast = head
            while slow != fast:
                fast = fast.next
                slow = slow.next

            return slow
        except:
            return None
        