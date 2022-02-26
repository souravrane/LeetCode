# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        curr = head
        '''
        Just like the way we construct 123 from "123". Base is 10
        1
        1*10 + 2
        12*10 + 3
        123
        
        We do the same for binary number. Base is 2
        '''
        while curr != None:
            res = res*2
            res += curr.val
            curr = curr.next
            
        return res
        