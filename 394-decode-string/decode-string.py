class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        for char in s:
            if char == ']':
                text = list()
                while stack[-1] != '[':
                    text.append(stack.pop())
                text.reverse()
                stack.pop()
                
                number = list()
                while stack and stack[-1].isnumeric():
                    number.append(stack.pop())
                
                number.reverse()
                finalText = ''.join(text)*int(''.join(number))
                stack.append(finalText)
            else:
                stack.append(char)
        return ''.join(stack)
        