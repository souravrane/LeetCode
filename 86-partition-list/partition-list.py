# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        
        cur = head
        left = right = dummy
        while cur:
            temp = cur.next
            cur.next = None

            if cur.val < x:
                if not left.next:
                    left.next = cur
                    left = left.next
                    right = right.next
                else:
                    cur.next = left.next
                    left.next = cur
                    left = left.next
            else:
                right.next = cur
                right = right.next
            
            cur = temp
        
        return dummy.next

        