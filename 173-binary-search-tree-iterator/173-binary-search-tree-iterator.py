# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def inOrder(self, root):
        if root == None:
            return 
        
        self.inOrder(root.left)
        self.arr.append(root.val)
        self.inOrder(root.right)
        
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.inOrder(root)        
        self.index = 0
        
    def next(self) -> int:
        value = self.arr[self.index]
        self.index += 1
        return value

    def hasNext(self) -> bool:
        return self.index < len(self.arr)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()