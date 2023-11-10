# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-1)
        total, carry = 0, 0
        temp = result

        while l1 or l2:
            if l1: 
                total += l1.val
                l1 = l1.next

            if l2: 
                total += l2.val
                l2 = l2.next

            acc = total + carry
            carry = acc // 10
            total = acc % 10
            
            temp.next = ListNode(total)
            temp = temp.next
            total = 0
        
        if carry: temp.next = ListNode(carry)

        return result.next

        
        