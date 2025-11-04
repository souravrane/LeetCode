# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        counter = defaultdict(int)
        cur = head
        while cur:
            counter[cur.val] += 1
            cur = cur.next
        
        prev, cur = dummy, head
        while True:
            while cur and counter[cur.val] > 1:
                prev.next = cur.next
                cur = cur.next
            
            if not cur: break
            
            prev = cur
            cur = cur.next
            
        return dummy.next 
