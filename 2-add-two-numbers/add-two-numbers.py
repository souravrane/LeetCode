# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        p1, p2, r = l1, l2, result
        carry = 0
        
        while p1 or p2:
            s = 0
            if p1:
                s += p1.val
                p1 = p1.next

            if p2: 
                s += p2.val
                p2 = p2.next

            s += carry
            carry =  s // 10
            s = s % 10
            r.next = ListNode(s)
            r = r.next

        if carry:
            r.next = ListNode(carry)

        return result.next