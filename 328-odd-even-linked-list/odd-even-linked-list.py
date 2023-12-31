# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddLL, evenLL = ListNode(), ListNode()
        index = 1
        cur = head
        odd, even = oddLL, evenLL

        while cur:
            if index % 2:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next

            cur = cur.next
            index += 1
        
        odd.next = None
        even.next = None

        odd.next = evenLL.next
        return oddLL.next

