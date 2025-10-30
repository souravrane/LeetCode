class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        bracket_map = {")":"(", "]":"[", "}":"{"}
        
        for b in s:
            if b in "([{": stack.append(b)
            elif not stack or stack[-1] != bracket_map[b]:
                return False
            else: stack.pop()

        return len(stack) == 0