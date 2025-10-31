class Solution:
    def add(self, a, b): return a + b

    def subtract(self, a, b): return a - b

    def multiply(self, a, b): return a * b

    def divide(self, a, b): return int(a / b)

    def operate(self, operand, a, b):
        expression = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }
        return expression[operand](a, b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        result = 0
        for token in tokens:
            if token in "+-/*":
                num2, num1 = stack.pop(), stack.pop()
                result = self.operate(token, num1, num2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]      