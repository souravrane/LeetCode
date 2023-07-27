class Solution:
    def _extractText(self, stack):
        text = []
        while(stack and stack[-1] != "["):
            char = stack.pop()
            text.append(char)
        if(stack): stack.pop()
        return ''.join(text[::-1])

    def _extractNum(self, stack):
        exp, value = 0, 0
        while(stack and stack[-1].isnumeric()):
            num = stack.pop()
            value += int(num)*pow(10,exp)
            exp += 1
        return value
        
    def decodeString(self, s: str) -> str:
        stack = list()
        for char in s:
            if(char == "]"):
                newSub = self._extractText(stack)
                number = self._extractNum(stack)
                stack.append(newSub*number)
            else:
                stack.append(char)
        return ''.join(stack)