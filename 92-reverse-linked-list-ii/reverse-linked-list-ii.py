# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # get the start position
        position = 1
        cur, start_connection = head, head
        while position < left:
            start_connection = cur
            cur = cur.next
            position += 1
        
        # start reversing
        tail = cur
        prev, end_connection = None, None
        while position <= right:
            end_connection = cur.next
            cur.next = prev
            prev = cur
            cur = end_connection
            position += 1

        start_connection.next = prev
        tail.next = end_connection
        
        if left > 1: return head
        return prev