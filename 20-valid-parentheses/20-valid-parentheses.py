class Solution:
    def isValid(self, s: str) -> bool:
        h = { "]":"[" , ")":"(", "}":"{" }
        stack = []
        top = -1
        for bracket in s:
            if bracket in ["(","[","{"]:
                stack.append(bracket)
                top += 1
            else:
                if top!= -1 and stack[top] == h[bracket]:
                    stack.pop()
                    top -= 1
                else:
                    return False
        
        if top == -1: return True
        return False
        