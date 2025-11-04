# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        p = q = dummy
        while n:
            q = q.next
            n -= 1
        
        while q.next:
            p = p.next
            q = q.next
        
        p.next = p.next.next
        return dummy.next