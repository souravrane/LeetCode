# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        curr = head
        x = -1
        while curr != None:
            x += 1
            curr = curr.next
        
        curr = head
        while curr != None:
            res += curr.val*(2**x)
            curr = curr.next
            x -= 1
        
        return res
        