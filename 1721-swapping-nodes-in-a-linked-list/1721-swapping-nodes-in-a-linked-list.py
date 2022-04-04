# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        
        firstNode = None
        lastNode = None
        
        curr = head
        while curr != None:
            length += 1
            if length == k:
                firstNode = curr
            curr = curr.next
        
        temp = 0
        curr = head
        while curr != None:
            temp += 1
            if temp == length - k + 1:
                lastNode = curr
                break
            curr = curr.next
            
        if(k == length-k+1): return head
        
        firstNode.val, lastNode.val = lastNode.val, firstNode.val
        
        return head
            
                
        