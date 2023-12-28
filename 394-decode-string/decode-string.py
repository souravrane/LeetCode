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
                
                number = 0
                i = 0
                while stack and stack[-1].isdigit():
                    number += int(stack[-1]) * pow(10,i)
                    stack.pop()
                    i += 1
                
                finalText = ''.join(text) * number
                stack.append(finalText)
            else:
                stack.append(char)
        return ''.join(stack)
        