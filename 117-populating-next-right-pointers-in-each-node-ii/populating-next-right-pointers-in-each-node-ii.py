class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        dq = deque([root])
        while dq:
            for i in range(1,len(dq)):
                dq[i-1].next = dq[i]

            for i in range(len(dq)):
                node = dq.popleft()
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
        return root            
