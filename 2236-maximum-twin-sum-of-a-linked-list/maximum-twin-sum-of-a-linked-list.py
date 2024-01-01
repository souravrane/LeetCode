# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        maxTwin = 0

        while fast.next:
            slow = slow.next
            fast = fast.next.next
        
        section1 = head
        section2 = slow.next
        slow.next = None

        section2 = self.reverseList(section2)

        while section1 and section2:
            maxTwin = max(maxTwin, section1.val + section2.val)
            section1 = section1.next
            section2 = section2.next

        return maxTwin
        
        