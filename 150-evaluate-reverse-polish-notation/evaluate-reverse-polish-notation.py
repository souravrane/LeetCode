class Solution:
    def calculate(self, op1, op2, operation):
        match operation:
            case "*":
                return op1 * op2
            case "/":
                return int(op1 / op2)
            case "+":
                return op1 + op2
            case "-":
                return op1 - op2
        return 0

    def evalRPN(self, tokens: List[str]) -> int:
        result = list()
        for token in tokens:
            if token not in "+-*/":
                result.append(int(token))
            else:
                op2 = result.pop()
                op1 = result.pop()
                result.append(self.calculate(op1, op2, token))
        return result[-1]