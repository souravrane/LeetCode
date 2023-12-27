class Solution:
    def removeStars(self, s: str) -> str:
        stack = list()
        for char in s:
            if char == '*': stack.pop()
            else: stack.append(char)
        return ''.join(stack)        