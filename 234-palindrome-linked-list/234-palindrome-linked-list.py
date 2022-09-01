# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp    
        return prev
    
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        secondHalf = self.reverseLL(temp)
        firstHalf = head
        
        while secondHalf:
            if firstHalf.val != secondHalf.val: return False 
            secondHalf = secondHalf.next
            firstHalf = firstHalf.next
        
        return True
        
        
            
    