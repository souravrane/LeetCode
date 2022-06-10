# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(-1)
        even = ListNode(-1)
        
        o = odd
        e = even
        
        flag = 1
        cur = head
        while cur:
            if flag:
                o.next = cur
                o = o.next
                cur = cur.next
                o.next = None
                
                flag = 0
            else:
                e.next = cur
                e = e.next
                cur = cur.next
                e.next = None
                
                flag = 1
                
            
        
        o.next = even.next
        return odd.next
 
                