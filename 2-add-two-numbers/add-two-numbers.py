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

        while p1 and p2:
            s = (carry + p1.val + p2.val) % 10
            carry =  (carry + p1.val + p2.val) // 10
            r.next = ListNode(s)
            r = r.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            s = (carry + p1.val) % 10
            carry = (carry + p1.val) // 10
            r.next = ListNode(s)
            r = r.next
            p1 = p1.next
        
        while p2:
            s = (carry + p2.val) % 10
            carry = (carry + p2.val) // 10
            r.next = ListNode(s)
            r = r.next
            p2 = p2.next
        
        if carry:
            r.next = ListNode(carry)

        return result.next