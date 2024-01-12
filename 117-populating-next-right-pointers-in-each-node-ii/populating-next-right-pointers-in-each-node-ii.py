class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        dq = deque([root])
        while dq:
            qLen = len(dq)
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
                if i != qLen - 1: node.next = dq[0]
        return root            