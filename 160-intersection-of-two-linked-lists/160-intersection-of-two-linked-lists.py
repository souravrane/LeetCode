# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        
        size1 = 0
        while p1:
            size1 += 1
            p1 = p1.next
        
        size2 = 0
        while p2:
            size2 += 1
            p2 = p2.next
        
        p1 = headA if size1 > size2 else headB
        p2 = headB if size1 > size2 else headA
            
        for i in range(abs(size1-size2)):
            p1 = p1.next
        
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
            
        
        