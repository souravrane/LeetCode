class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        top = -1
        max_depth = 0
        
        '''
        everytime we encounter a closing bracket, the height of the stack at that point
        will tell us what level of nesting was present so far.
        
        '''
        for char in s:
            if char == "(":
                stack.append(char)
                top += 1
            elif char == ")":
                max_depth = max(max_depth,top+1)
                stack.pop()
                top -= 1
        
        return max_depth