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
        while l1 != None and l2 != None:
            s = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            
            newNode = ListNode(s)
            curr.next = newNode
            curr = newNode
            
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None :
            s = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            
            newNode = ListNode(s)
            curr.next = newNode
            curr = newNode
            
            l1 = l1.next
        
        while l2 != None :
            s = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            
            newNode = ListNode(s)
            curr.next = newNode
            curr = newNode
            
            l2 = l2.next
            
        if carry != 0:
            newNode = ListNode(carry)
            curr.next = newNode
        
        return head.next
            
        
            
            