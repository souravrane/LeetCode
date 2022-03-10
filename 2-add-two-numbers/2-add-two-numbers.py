# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(None)
        curr = head
        while l1 != None or l2 != None or carry:
            num1,num2 = 0,0
            
            if l1 != None:
                num1 = l1.val
                l1 = l1.next
            
            if l2 != None:
                num2 = l2.val
                l2 = l2.next
            
            s = (num1 + num2 + carry) % 10
            carry = (num1 + num2 + carry) // 10
 
            newNode = ListNode(s)
            curr.next = newNode
            curr = newNode
       
       
        
        return head.next
            
        
            
            