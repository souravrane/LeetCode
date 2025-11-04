# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_kth_node(self, cur, k):
        while cur and k:
            cur = cur.next
            k -= 1
        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        prev_group = dummy
        cur = head
        while True:
            kth_node = self.get_kth_node(prev_group, k)
            
            if not kth_node: break
            next_group = kth_node.next
            
            prev = kth_node.next
            cur = prev_group.next
            while cur != next_group:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = prev_group.next
            prev_group.next = kth_node
            prev_group = temp

        return dummy.next