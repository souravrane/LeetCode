"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        result = Node(-1)
        r = result
        h = head
        
        og_order = dict() # addr - pos

        og_map = dict()
        new_map = dict() # pos - addr

        # List is cloned
        order = 1
        while h:
            r.next = Node(h.val)
            og_order[h] = order
            new_map[order] = r.next

            order += 1
            h = h.next
            r = r.next
        
        og_order[None] = -1
        new_map[-1] = None
        # random pointer order determined
        h = head
        while h:
            random_pos = og_order[h.random]
            og_map[h] = random_pos
            h = h.next

        # random pointer mapping
        r = result.next
        h = head
        while h:
            pos_to_point = og_map[h]
            node_at_pos = new_map[pos_to_point]
            r.random = node_at_pos
            h = h.next
            r = r.next
        
        return result.next

        

