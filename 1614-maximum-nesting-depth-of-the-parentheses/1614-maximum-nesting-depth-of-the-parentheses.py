

'''
Method 1 : space: O(N) Time: O(N)
Everytime we encounter a closing bracket in the stack, the height of the stack at that point
will tell us what level of nesting was present so far before we pop it off.

Method 2: space: O(1) Time: O(N)
When we find left bracket add 1 to the count, right bracket subtract 1 from the count.
Keep updating the global max everytime you count a left bracket. The answer would be the maximum
left brackets at any given point.

'''
class Solution:
    def maxDepth(self, s: str) -> int:
        
        bracket_count = 0
        max_depth = 0
        for char in s:
            if char == "(":
                bracket_count += 1
                max_depth = max(bracket_count,max_depth)
            elif char == ")":
                bracket_count -= 1
        
        return max_depth