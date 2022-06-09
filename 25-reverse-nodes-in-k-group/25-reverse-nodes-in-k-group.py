# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKth(self, cur, k):
        while cur and k:
            cur = cur.next
            k -= 1
        return cur
    
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prevGroup = dummy
        
        while True:
            kthNode = self.getKth(prevGroup, k)
            
            if kthNode == None: break
            nextGroup = kthNode.next
            
            # reverse the group
            prev = kthNode.next
            cur = prevGroup.next
            
            while cur != nextGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            # setting the last node of prev group after reversal
            temp = prevGroup.next
            prevGroup.next = kthNode
            prevGroup = temp
        
        return dummy.next
            
            
            
    
    