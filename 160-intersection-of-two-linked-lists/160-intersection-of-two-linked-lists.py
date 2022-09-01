# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ll1Len = ll2Len = 0
        cur = headA
        while cur:
            ll1Len += 1
            cur = cur.next
            
        cur = headB
        while cur:
            ll2Len += 1
            cur = cur.next
        
        # keep headA to be the longest ll
        if(ll2Len > ll1Len):
            headA, headB = headB, headA
        
        difference = abs(ll2Len - ll1Len)
        while difference:
            headA = headA.next
            difference -= 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
        