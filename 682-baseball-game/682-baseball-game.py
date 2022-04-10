class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for char in ops:
            if char.isnumeric() or char[0] == "-":
                stack.append(int(char))
                
            elif char == "+":
                stack.append(stack[-1] + stack[-2]) 
                
            elif char == "D":
                stack.append(2*stack[-1])
                
            elif char == "C":
                stack.pop()
        
        return sum(stack)